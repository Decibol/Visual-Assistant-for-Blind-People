from frontend import VisionAssistantApp
from object_detector import ObjectDetector
# In main.py replace LLMProcessor import with:
from local_llm import LocalLLMProcessor
from tts import TTS
import cv2
import tkinter as tk

class VisionProcessor:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.frame_count = 0
        self.object_detector = ObjectDetector()
        self.llm_processor = LLMProcessor()
        self.tts = TTS()
        
    def detect_objects(self, frame):
        return self.object_detector.detect_objects(frame)
        
    def generate_description(self, detections):
        return self.llm_processor.generate_description(detections)
        
    def speak_description(self, text):
        self.tts.speak(text)

def main():
    root = tk.Tk()
    processor = VisionProcessor()
    app = VisionAssistantApp(root, processor)
    root.mainloop()
    
    # Release resources
    processor.cap.release()

if __name__ == "__main__":
    main()