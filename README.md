# Hand Vision Thread

> Computer vision-based hand gesture recognition system with remote camera support

## 🎯 Overview

A system that allows for the use of MediaPipe's hand detection and landmark features without delay with streaming video shot remotely. Establish a Remote Connection Between a PC and a Mobile Phone Using Threading to Manage Latency.

This project provides real-time hand gesture recognition and landmark detection using MediaPipe, with support for various camera sources including webcams, mobile phones (via DroidCam), and ESP32-CAM modules.

Incorporates the 'Hand Tracking Module' from Computer Vision Zone [https://www.computervision.zone/]

## 📁 Project Structure

```
hand-vision-thread/
├── HandGesture/          # Gesture recognition module
│   ├── main.py          # Main gesture recognition script
│   ├── GestureModule.py # Gesture handler class
│   ├── config.py        # Configuration management
│   └── requirements.txt
├── HandLandMark/        # Hand landmark detection module
│   ├── main.py          # Main landmark detection script
│   ├── HandTrackingModule.py
│   └── requirements.txt
├── .env.example         # Environment variables template
├── .gitignore          # Git ignore rules
└── README.md
```

## 🚀 Quick Start

### 1. Setup Environment

```bash
# Clone the repository
git clone https://github.com/tinmanlab/hand-vision-thread.git
cd hand-vision-thread

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies (choose one)
cd HandGesture && pip install -r requirements.txt
# OR
cd HandLandMark && pip install -r requirements.txt
```

### 2. Configure Settings

Copy `.env.example` to `.env` and configure:

```bash
cp .env.example .env
```

Edit `.env` with your settings:
```env
# For Webcam
CAMERA_URL=0

# For DroidCam
CAMERA_URL=http://192.168.1.100:4747/video

# For ESP32-CAM
CAMERA_URL=http://192.168.1.200:81/stream

# Serial settings (optional)
SERIAL_PORT=COM9
SERIAL_BAUDRATE=115200
```

### 3. Run the Application

```bash
# For gesture recognition
cd HandGesture
python main.py

# For landmark detection
cd HandLandMark
python main.py
```

Press 'q' to quit the application.

## 🔧 Configuration

### Camera Sources

1. **Webcam**: Set `CAMERA_URL=0` in `.env`
2. **DroidCam**: 
   - Install [DroidCam app](https://play.google.com/store/apps/details?id=com.dev47apps.obsdroidcam) on your phone
   - Connect phone and PC to same network
   - Use phone's IP address in `.env`
3. **ESP32-CAM**: 
   - Configure your ESP32-CAM module with appropriate firmware
   - Use ESP32's IP address in `.env`

### Serial Communication (Optional)

For robot control via serial port, uncomment the serial code in `main.py` and configure:
```env
SERIAL_PORT=COM9        # Windows
# SERIAL_PORT=/dev/ttyUSB0  # Linux
SERIAL_BAUDRATE=115200
```

## 📋 Features

### Hand Gesture Recognition (`HandGesture/`)
- Recognizes 8 different gestures:
  - Unknown (0)
  - Closed Fist (1)
  - Open Palm (2)
  - Pointing Up (3)
  - Thumb Down (4)
  - Thumb Up (5)
  - Victory (6)
  - ILoveYou (7)
- Real-time gesture detection with confidence scores
- Low-pass filtering for stable detection
- Visual feedback with bounding boxes

### Hand Landmark Detection (`HandLandMark/`)
- Tracks 21 hand landmarks in real-time
- Calculates distances between landmarks
- Suitable for robot control applications
- Real-time visualization of hand skeleton

## 🛠️ Troubleshooting

| Issue | Solution |
|-------|----------|
| Camera not connecting | Check IP address and port in `.env`, ensure devices are on same network |
| Low FPS | Reduce detection confidence or use lower resolution |
| Serial port error | Ensure correct COM port and permissions, check Device Manager (Windows) |
| ModuleNotFoundError | Activate virtual environment and install requirements |
| Model file missing | Ensure `gesture_recognizer.task` is in HandGesture folder |

## 📦 Dependencies

- Python 3.8+
- OpenCV (`opencv-contrib-python`)
- MediaPipe (`mediapipe`)
- NumPy (`numpy`)
- python-dotenv (for configuration)
- pyserial (optional, for robot control)

## 🔒 Security Notes

- Never commit `.env` files with actual IP addresses or credentials
- Use `.env.example` as a template
- Keep your network cameras secured with proper authentication

## 📄 License

MIT License - see LICENSE file for details

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## 🙏 Acknowledgments

- [MediaPipe](https://developers.google.com/mediapipe) by Google
- [Computer Vision Zone](https://www.computervision.zone/) for Hand Tracking Module
- [DroidCam](https://www.dev47apps.com/) for mobile camera streaming

---
*Developed with MediaPipe and OpenCV*
*Last updated: 2025-08-11*