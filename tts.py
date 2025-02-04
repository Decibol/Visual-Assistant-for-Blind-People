import pyttsx3
import threading

class TTS:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)
        self.engine.setProperty('volume', 1.0)
        
    def speak(self, text):
        def run():
            self.engine.say(text)
            self.engine.runAndWait()
        thread = threading.Thread(target=run)
        thread.start()