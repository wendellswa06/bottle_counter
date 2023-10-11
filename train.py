import torch
from ultralytics import YOLO

model = YOLO('yolov8l.pt')

results = model.train(data='./licence_plate.yaml', name='licence_plate', epochs=100, patience=20, batch=16, cache=True, imgsz=640, iou=0.5, augment=True, degrees=25.0, fliplr=0.0, lr0=0.0001, optimizer='Adam')