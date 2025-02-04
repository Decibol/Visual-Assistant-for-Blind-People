# Visual-Assistant-for-Blind-People
An LLM-powered visual assistant for partially or fully blind people that processes any video feed and describes the objects in it through text-to-speech.

## Installation
1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt

## Usage
1. Run the application:
   ```bash
   python main.py
2. Click "Start" to begin processing
3. The system will:
   - Show live camera feed with object detection
   - Generate verbal descriptions every 2 seconds
   - Speak descriptions aloud through text-to-speech

## Features
- Real-time object detection using YOLOv8
- Context-aware scene descriptions using GPT-3.5
- Text-to-speech with adjustable settings
- Simple GUI with start/stop control
