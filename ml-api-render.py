from flask import Flask, request, jsonify
from yolov5.yolov5 import Model

app = Flask(__name__)

yolov5 = Model()
print("Success! yolov5 model init")

@app.route('/v1/yolov5', methods=['GET'])
def run_yolov5():
    SAVE_DIR = 'result/yolov5/pic'
    imageURL = 'https://ultralytics.com/images/zidane.jpg'   # TODO: 可変に

    imgBase64 = yolov5.model_render(SAVE_DIR, imageURL)

    # JSON形式でレスポンス
    return jsonify(imgBase64)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port = 8080)   # ポート番号を開けておく
