import cv2
from ultralytics import YOLO
import numpy as np

class ObjectDetector:
    def __init__(self):
        self.model = YOLO('yolov8n.pt')
        self.classes = self.model.names

    def detect_objects(self, frame):
        results = self.model(frame)
        detections = []
        
        for result in results:
            boxes = result.boxes.xyxy.cpu().numpy()
            confidences = result.boxes.conf.cpu().numpy()
            class_ids = result.boxes.cls.cpu().numpy().astype(int)
            
            for box, conf, cls_id in zip(boxes, confidences, class_ids):
                label = self.classes[cls_id]
                detections.append({
                    'label': label,
                    'confidence': float(conf),
                    'position': box.tolist()
                })
        
        return detections, results[0].plot()