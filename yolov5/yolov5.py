import torch
import base64
import io
from PIL import Image
import time

def model(saveDir, imageURL):
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
    results = model(imageURL)
    results.save(save_dir = saveDir)

    return results

def model_render(saveDir, imageURL):
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
    results = model(imageURL)

    # image to base64
    buffered = io.BytesIO()
    img_base64 = Image.fromarray(results.ims[0])
    img_base64.save(buffered, format="JPEG")
    print(base64.b64encode(buffered.getvalue()).decode('utf-8')) 

    return base64.b64encode(buffered.getvalue()).decode('utf-8')
