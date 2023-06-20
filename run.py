from ultralytics import YOLO


yolo task=detect mode=predict model="weights/best.pt" source=0 conf=0.50
