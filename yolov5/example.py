"""
前提
    - conda環境がある
    - yolov5用の requirements をダウンロードしている
        - git clone https://github.com/ultralytics/yolov5
        - yolov5 > requirements.txt
    - 本プロジェクトにおいては requirements をダウンロード済み

コマンド
    $ conda create -n ml-api python=3.8
    $ conda activate ml-api
    $ cd yolov5
    $ pip install -qr requirements.txt
    $ python example.py
"""

import torch

SAVE_DIR = "result/pic"
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
img = 'https://ultralytics.com/images/zidane.jpg'
results = model(img)
results.save(save_dir = SAVE_DIR)