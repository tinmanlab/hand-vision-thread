# Compatible Android app
# https://play.google.com/store/apps/details?id=com.dev47apps.obsdroidcam

import cv2
from HandTrackingModule import HandDetector
from QuickCaptureModule import Capture

detector = HandDetector(maxHands=1, detectionCon=0.5, minTrackCon=0.5)

# Use the TCP/IP address of your mobile phone
#cap = Capture('http://192.168.?.?:?/video')

# Default camera view on your PC
cap = Capture()

if __name__ == "__main__":

    while True:
        frame = cap.read()

        # Process frame
        #rotated_img = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
        #hands, img = detector.findHands(cv2.flip(rotated_img, 1))
        
        hands, img = detector.findHands(frame)

        cv2.imshow('', img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
