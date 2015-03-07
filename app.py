#-*- coding:utf-8 -*-
from app import app
"""
#flaskパッケージのFlaskクラスをインポート
from flask import Flask
#Flaskインスタンスを作成
app = Flask(__name__)

#routeデコレータを使い、/というURL遺体しての処理を追加
@app.route('/')
def index():
    return 'hello world!'
"""
if __name__ == '__main__':
    #debug = Trueでデバッグモードで起動する。
    app.run(debug=True, host = '127.0.0.1', port = 4444)