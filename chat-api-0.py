"""
環境構築確認用
"""

from flask import Flask, request, jsonify, render_template, make_response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port = 8080)
