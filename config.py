#coding:utf-8
#flaskの設定ファイルが置いてある場所
#データベースの設定と、セッション情報を暗号化するためのキーを設定
import os

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI ='sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
CSRF_ENABLED = True
SECRET_KEY = 'hogehogehogepiyohoge'
