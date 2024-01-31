# Compatible Android app
# https://play.google.com/store/apps/details?id=com.dev47apps.obsdroidcam

import math
import cv2
import numpy as np
import serial

from HandTrackingModule import HandDetector
from QuickCaptureModule import Capture
#from SerialModule import SerialObject

detector = HandDetector(maxHands=1, detectionCon=0.5, minTrackCon=0.5)

# Use the TCP/IP address of your mobile phone
#cap = Capture('http://192.168.?.?:?/video')

# teensy connected to COM16
#teensy = serial.Serial(port='COM9', baudrate=115200, timeout=0, writeTimeout=0)
length = 0

# Default camera view on your PC
cap = Capture()

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
            
            #teensy.write('*1,{}\n'.format(repr(length)).encode('Ascii'))

        cv2.imshow('', img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
