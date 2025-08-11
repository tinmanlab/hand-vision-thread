# HandLandMark - Real-time Hand Tracking

Real-time hand landmark detection and tracking using MediaPipe for precise hand position analysis.

## 🎯 Overview

This module provides accurate hand landmark detection, tracking 21 key points on each hand in real-time. It enables precise hand pose estimation, finger tracking, and gesture analysis for advanced human-computer interaction applications.

## ✨ Features

- **21 Landmark Detection**: Tracks all major hand joints and fingertips
- **Multi-hand Support**: Detect and track up to 2 hands simultaneously
- **Serial Communication**: Send landmark data to hardware devices
- **Thread-safe Architecture**: Optimized multi-threaded capture and processing
- **Real-time Performance**: 30+ FPS on standard hardware

## 📦 Installation

### Prerequisites
- Python 3.8 or later
- Webcam or camera device
- (Optional) Serial device for hardware integration

### Setup Steps

1. **Clone the repository**
```bash
git clone https://github.com/tinmanlab/hand-vision-thread.git
cd hand-vision-thread/HandLandMark
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

### Python Integration
```python
from HandTrackingModule import HandDetector

# Initialize detector
detector = HandDetector(maxHands=2, detectionCon=0.7)

# Process frame
hands, img = detector.findHands(frame)
if hands:
    hand = hands[0]
    landmarks = hand["lmList"]  # 21 landmarks
    bbox = hand["bbox"]          # Bounding box
    centerPoint = hand["center"] # Center of hand
```

### Serial Communication
```python
from SerialModule import SerialCommunicator

# Initialize serial connection
serial_comm = SerialCommunicator(port='COM3', baudrate=115200)

# Send landmark data
serial_comm.send_landmarks(landmarks)
```

## 🎮 Landmark Points

The module detects 21 landmarks per hand:

```
0: WRIST
1-4: THUMB (CMC, MCP, IP, TIP)
5-8: INDEX_FINGER (MCP, PIP, DIP, TIP)
9-12: MIDDLE_FINGER (MCP, PIP, DIP, TIP)
13-16: RING_FINGER (MCP, PIP, DIP, TIP)
17-20: PINKY (MCP, PIP, DIP, TIP)
```

## 📁 Project Structure
```
HandLandMark/
├── main.py                   # Main application
├── HandTrackingModule.py     # Hand detection and tracking
├── QuickCaptureModule.py     # Thread-safe camera capture
├── SerialModule.py           # Serial communication
├── requirements.txt          # Dependencies
└── README.md                # This file
```

## 🔧 Configuration

### Detection Parameters
```python
detector = HandDetector(
    mode=False,           # Static/Video mode
    maxHands=2,          # Maximum hands to detect
    detectionCon=0.5,    # Detection confidence (0-1)
    trackCon=0.5         # Tracking confidence (0-1)
)
```

### Camera Settings
```python
# Change camera source in main.py
cap = cv2.VideoCapture(0)  # Default camera
# cap = cv2.VideoCapture('http://192.168.1.100:8080/video')  # IP camera
```

## 🔌 API Reference

### HandTrackingModule.HandDetector

**Methods:**
- `findHands(img, draw=True)` - Detect hands and optionally draw landmarks
- `findPosition(img, handNo=0)` - Get landmarks for specific hand
- `fingersUp()` - Detect which fingers are raised
- `findDistance(p1, p2, img)` - Calculate distance between two landmarks

### SerialModule.SerialCommunicator

**Methods:**
- `connect()` - Establish serial connection
- `send_data(data)` - Send data to device
- `read_data()` - Read data from device
- `disconnect()` - Close serial connection

## 📊 Performance

- **Detection Speed**: ~30ms per frame
- **Accuracy**: 95%+ in good lighting
- **CPU Usage**: 20-30% on quad-core
- **Memory**: ~150MB RAM

## 🐛 Troubleshooting

### Common Issues

1. **No hands detected**
   - Improve lighting conditions
   - Adjust detection confidence
   - Ensure hands are fully visible

2. **Serial connection failed**
   - Check COM port availability
   - Verify baudrate settings
   - Install serial drivers if needed

3. **Low FPS**
   - Reduce image resolution
   - Lower maxHands parameter
   - Close other applications

## 🔗 Applications

- Robot hand control
- Sign language recognition
- Virtual keyboard/mouse
- Gesture-based interfaces
- Hand rehabilitation systems

## 📄 License

MIT License - See LICENSE file for details

## 👥 Authors

- TinmanLab Research Team

---

For more information, see the [main repository README](../README.md)