import tkinter as tk
from PIL import Image, ImageTk
import cv2

class VisionAssistantApp:
    def __init__(self, root, processor):
        self.root = root
        self.processor = processor
        self.is_running = False
        
        # GUI Setup
        self.root.title("Vision Assistant")
        self.root.geometry("800x600")
        
        # Video Display
        self.video_label = tk.Label(root)
        self.video_label.pack(expand=True, fill=tk.BOTH)
        
        # Controls
        self.control_frame = tk.Frame(root)
        self.control_frame.pack(pady=10)
        
        self.start_btn = tk.Button(self.control_frame, text="Start", command=self.toggle_processing)
        self.start_btn.pack(side=tk.LEFT, padx=5)
        
        self.desc_label = tk.Label(root, text="Description will appear here", wraplength=700)
        self.desc_label.pack(pady=10)
        
    def toggle_processing(self):
        self.is_running = not self.is_running
        self.start_btn.config(text="Stop" if self.is_running else "Start")
        if self.is_running:
            self.process_frames()
            
    def process_frames(self):
        if self.is_running:
            ret, frame = self.processor.cap.read()
            if ret:
                detections, processed_frame = self.processor.detect_objects(frame)
                self.update_frame(processed_frame)
                
                if self.processor.frame_count % 30 == 0:  # Process every second (assuming 30fps)
                    description = self.processor.generate_description(detections)
                    self.desc_label.config(text=description)
                    self.processor.speak_description(description)
                
                self.processor.frame_count += 1
                
            self.root.after(10, self.process_frames)
            
    def update_frame(self, frame):
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img)
        self.video_label.imgtk = imgtk
        self.video_label.config(image=imgtk)