#coding:utf-8
"""
request:    HTTPリクエストオブジェクト methodやフォームデータにアクセスできる
session:    暗号化されたcookieで実装された辞書
render_template:
    指定したHTMLテンプレートを使ってレスポンスを返す。
redirect:   指定したURLにリダイレクトするレスポンスを返す。
url_for:    指定したエンドポイントに対するURLを返す。
abort:  指定したHTTPステータスコードのエラーを返す。
flash:  メッセージを通知するための仕組み
"""
from functools import wraps
from flask import (request, redirect, url_for, render_template, flash,jsonify, abort, session,g)
from app import app, db
from app.models import *
import sys
import os
import MeCab

@app.route('/')
def show_entries():
    m = MeCab.Tagger("-Ochasen")
    string = u'Pythonで作る検索エンジン'
    string = string.encode("utf-8")
    node = m.parseToNode(string)
    a = []
    while node:
        a.append(node.surface.decode())
        node = node.next

    entries = Entry.query.order_by(Entry.id.desc()).all()
    articles = Article.query.order_by(Article.id.desc()).all()
    #test = articles[1]
    return render_template('show_entries.html', entries=entries, articles=articles, text = a )

@app.route('/show_cook/')
def show_cook():
    articles = Article.query.order_by(Article.id.desc()).all()
    cookpad_articles = Article.query.filter_by(is_cook = 1 ).all()
    return render_template('show_cook.html', articles=cookpad_articles )

@app.route('/show_nikkei/')
def show_nikkei():
    articles = Article.query.order_by(Article.id.desc()).all()
    nikkei_articles = Article.query.filter_by(is_nikkei = 1).all()
    return render_template('show_nikkei.html', articles=nikkei_articles )

@app.route('/article_detail/<int:article_id>/')
def article_detail(article_id):
    article = Article.query.get(article_id)
    #articles = Article.query.order_by(Article.id.desc()).all()
    #nikkei_articles = Article.query.filter_by(is_nikkei = 1).all()
    return render_template('article_detail.html', article=article )


@app.route('/add', methods=['POST'])
def add_entry():
    entry= Entry(
        title = request.form['title'],
        text = request.form['text']
        )
    db.session.add(entry)
    db.session.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))

@app.route('/users/')
def user_list():
    users = User.query.all()
    return render_template('user/list.html', users = users)

@app.route('/users/<int:user_id>/')
def user_detail(user_id):
    user = User.query.get(user_id)
    return render_template('user/detail.html', user=user)

@app.route('/users/<int:user_id>/edit/', methods = ['GET', 'POST'])
def user_edit(user_id):
    user = User.query.get(user_id)
    if user is None:
        abort(404)
    if request.method == 'POST':
        user.name=request.form['name']
        user.email=request.form['email']
        user.password=request.form['password']
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('user_detail', user_id = user.id))
    return render_template('user/edit.html', user=user)

@app.route('/users/create', methods = ['GET', 'POST'])
def user_create():
    if request.method == 'POST':
        user = User(
            name = request.form['name'],
            email = request.form['email'],
            password = request.form['password']
            )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('user_list'))
    return render_template('user/edit.html')

@app.route('/users/<int:user_id>/delete/', methods=['DELETE'])
def user_delete(user_id):
    user = User.query.get(user_id)
    if user is None:
        response = jsonify({'status': 'Not Found'})
        response.status_code = 404
        return response
    db.session.delete(user)
    db.session.commit()
    return jsonify({'status': 'OK'})