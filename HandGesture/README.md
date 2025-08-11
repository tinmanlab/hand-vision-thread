# HandGesture - Real-time Gesture Recognition

Real-time hand gesture recognition using MediaPipe for intuitive human-computer interaction.

## 🎯 Overview

This module provides robust hand gesture recognition capabilities using Google's MediaPipe framework. It can detect and classify various hand gestures in real-time from camera feeds, enabling gesture-based control interfaces.

## ✨ Features

- **Real-time Recognition**: Process camera feeds at 30+ FPS
- **Multiple Gesture Support**: Recognizes common gestures (thumbs up/down, victory, pointing, etc.)
- **Thread-safe Capture**: Efficient frame capture using threading
- **Low Latency**: Optimized for responsive interaction
- **Cross-platform**: Works on Windows, Linux, and macOS

## 📦 Installation

### Prerequisites
- Python 3.10.7 or later
- Webcam or camera device

### Setup Steps

1. **Clone the repository**
```bash
git clone https://github.com/tinmanlab/hand-vision-thread.git
cd hand-vision-thread/HandGesture
```

2. **Create virtual environment**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

## 🚀 Usage

### Quick Start
```bash
python main.py
```

### Camera Configuration
Edit `main.py` to change camera source:
```python
# Default camera
cap = cv2.VideoCapture(0)

# IP camera
cap = cv2.VideoCapture('http://192.168.1.100:8080/video')
```

## 📁 Project Structure
```
HandGesture/
├── main.py                    # Main application
├── GestureModule.py          # Gesture recognition logic
├── QuickCaptureModule.py     # Thread-safe camera capture
├── gesture_recognizer.task   # MediaPipe model file
└── requirements.txt          # Dependencies
```

## 🔗 References

- [MediaPipe Gesture Recognition](https://developers.google.com/mediapipe/solutions/vision/gesture_recognizer)

## 📄 License

MIT License


