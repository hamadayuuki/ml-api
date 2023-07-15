import torch

def model(saveDir, imageURL):
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
    results = model(imageURL)
    results.save(save_dir = saveDir)

    return results