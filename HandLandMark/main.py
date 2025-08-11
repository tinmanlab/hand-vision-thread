# Compatible Android app
# https://play.google.com/store/apps/details?id=com.dev47apps.obsdroidcam

import math
import cv2
import numpy as np
import os
from dotenv import load_dotenv
# import serial  # Uncomment if using serial communication

from HandTrackingModule import HandDetector
from QuickCaptureModule import Capture
# from SerialModule import SerialObject  # Uncomment if using SerialModule

# Load environment variables
load_dotenv()

# Configuration
max_hands = int(os.getenv('MAX_HANDS', 1))
detection_conf = float(os.getenv('DETECTION_CONFIDENCE', 0.5))
tracking_conf = float(os.getenv('TRACKING_CONFIDENCE', 0.5))
camera_url = os.getenv('CAMERA_URL', '0')

# Initialize detector
detector = HandDetector(maxHands=max_hands, detectionCon=detection_conf, minTrackCon=tracking_conf)

# Initialize camera
if camera_url == '0':
    cap = Capture()  # Webcam
else:
    cap = Capture(camera_url)  # Network camera

# Serial configuration (uncomment if needed)
# serial_port = os.getenv('SERIAL_PORT', 'COM9')
# serial_baudrate = int(os.getenv('SERIAL_BAUDRATE', 115200))
# teensy = serial.Serial(port=serial_port, baudrate=serial_baudrate, timeout=0, writeTimeout=0)

length = 0

if __name__ == "__main__":

    while True:
        frame = cap.read()

        # Process frame
        #rotated_img = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
        #hands, img = detector.findHands(cv2.flip(rotated_img, 1))
        
        hands, img = detector.findHands(frame)

        if hands:
            lmList = hands[0]['lmList']
            #print(lmList[4], lmList[8])
            
            x1, y1 ,z1 = lmList[4]
            x2, y2, z2 = lmList[8]

            cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
            length = math.hypot(x2 - x1, y2 - y1)
            length = int(((length // 10) * 10 - 30)*0.1)

            if length < 0: length = 0
            if length > 10: length = 10
            
            print(length)
            
            # Send data via serial if connected
            # if 'teensy' in locals():
            #     teensy.write('*1,{}\n'.format(repr(length)).encode('Ascii'))

        cv2.imshow('', img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
