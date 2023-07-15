from flask import Flask, request, jsonify
from yolov5.yolov5 import model

app = Flask(__name__)

@app.route('/v1/yolov5', methods=['GET'])
def run_yolov5():
    SAVE_DIR = 'result/yolov5/pic'
    imageURL = 'https://ultralytics.com/images/zidane.jpg'   # TODO: 可変に

    results = model(SAVE_DIR, imageURL)

    # JSON形式でレスポンス
    return jsonify(str(results))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port = 8080)   # ポート番号を開けておく
