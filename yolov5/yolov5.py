import torch
import base64
import io
from PIL import Image

def model(saveDir, imageURL):
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
    results = model(imageURL)
    results.save(save_dir = saveDir)

    return results

def model_render(saveDir, imageURL):
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
    results = model(imageURL)
    results.render()  # results.xyxyに対する境界ボックスを描画
    imgPil = Image.fromarray(results.rendered.astype('uint8'))  # PIL Imageオブジェクトへ変換

    # image to base64
    buffered = io.BytesIO()
    imgPil.save(buffered, format="JPEG")  # 画像をJPEG形式で保存
    imgBase64 = base64.b64encode(buffered.getvalue()).decode()  # base64形式にエンコードして文字列に変換

    return imgBase64