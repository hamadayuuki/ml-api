import torch
import base64
import io
from PIL import Image
import time

class Model:
    def __init__(self):
        self.model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

    def model(self, saveDir, imageURL):
        results = self.model(imageURL)
        results.save(save_dir = saveDir)

        return results

    def model_render(self, saveDir, imageURL):
        results = self.model(imageURL)

        # image to base64
        buffered = io.BytesIO()
        img_base64 = Image.fromarray(results.ims[0])
        img_base64.save(buffered, format="JPEG")
        print(base64.b64encode(buffered.getvalue()).decode('utf-8')) 

        return base64.b64encode(buffered.getvalue()).decode('utf-8')