"""
データベースの処理として必須であるCRUDを実装する
今回データはリストとして保持する
本来は データを永続化するため、DBへ格納する

CRUD
    - Create : 作成
    - Read : 読み出し
    - Update : 更新
    - Delete : 削除

リストの例
[
    {
        "message": "update",
        "name": "me"
    },
    {
        "message": "update",
        "name": "me"
    },
    ・・・
]
"""

from flask import Flask, request, jsonify, render_template, make_response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

messages = []

@app.route('/')
def index():
    return render_template('index.html')

# C : Create
@app.route('/v1/create', methods=['GET'])
def create():
    messages = [{"name": "me", "message": "create!"}]
    return jsonify(messages)

# R : Read
@app.route('/v1/read', methods=['GET'])
def read():
    return jsonify(messages)

# U : Update
@app.route('/v1/update', methods=['GET'])
def update():
    message = {"name": "me", "message": "update"}
    messages.append(message)
    return jsonify(messages)

# D : Delete
@app.route('/v1/delete', methods=['GET'])
def delete():
    del messages[-1]   # 末尾のメッセージ
    return jsonify(messages)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port = 8080)
