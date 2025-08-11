# Reference : https://developers.google.com/mediapipe/solutions/vision/gesture_recognizer

import cv2
import mediapipe as mp
import time
import os
from dotenv import load_dotenv
# import serial  # Uncomment if using serial communication

from QuickCaptureModule import Capture
from GestureModule import GestureHandler

# Load environment variables
load_dotenv()

# Configuration
model_path = os.getenv('MODEL_PATH', 'gesture_recognizer.task')
camera_url = os.getenv('CAMERA_URL', '0')

# Open a video capture stream
if camera_url == '0':
    cap = Capture()  # Webcam
else:
    cap = Capture(camera_url)  # Network camera

# Serial configuration (uncomment if needed)
# serial_port = os.getenv('SERIAL_PORT', 'COM9')
# serial_baudrate = int(os.getenv('SERIAL_BAUDRATE', 115200))
# teensy = serial.Serial(port=serial_port, baudrate=serial_baudrate, timeout=0, writeTimeout=0)

# Set the callback function to handle the gesture recognition result
handler = GestureHandler(cap)

# Set up the gesture recognizer options
options = mp.tasks.vision.GestureRecognizerOptions(
    base_options=mp.tasks.BaseOptions(model_asset_path=model_path),
    running_mode=mp.tasks.vision.RunningMode.LIVE_STREAM,
    num_hands=1,
    min_hand_detection_confidence=0.5,
    min_hand_presence_confidence=0.5,
    min_tracking_confidence=0.5,
    result_callback=handler.print_result)

# Initialize the gesture recognizer
with mp.tasks.vision.GestureRecognizer.create_from_options(options) as recognizer:

    frame_count = 0  # Initialize frame_count before the loop
    visual_queue = 0 # Initialize visual_queue before the loop

    time.sleep(0.1)

    while cap.isOpened():

        image = cap.read()

        # Flip the image horizontally for a later selfie-view display
        #image = cv2.flip(image, 1)

        # Convert the BGR image to RGB
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Process the image and perform gesture recognition
        frame_count += 1
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=image_rgb)
        recognizer.recognize_async(mp_image, timestamp_ms=frame_count)
        #recognizer.recognize_async(mp_image, timestamp_ms=cap.get_timestamp_ms())

        # Frame rate (FPS)
        handler.get_frame(image)

        if handler.is_detected():
            
            gesture_detected = 0

            # Gesture labels mapping:
            # 0 - Unknown
            # 1 - Closed_Fist
            # 2 - Open_Palm
            # 3 - Pointing_Up
            # 4 - Thumb_Down
            # 5 - Thumb_Up
            # 6 - Victory
            # 7 - ILoveYou    
            if handler.get_label() == "Thumb_Up":
                gesture_detected = handler.get_score()
                #gesture_detected = 1

            # Low Pass Filter
            visual_queue = gesture_detected*0.1+visual_queue*0.9
            text_label = "Released"
            
            # When the score is greater than 0.5, we can say that the gesture is maintained
            if visual_queue > 0.5:
                text_label = "Grasp"
                # Control the robot arm if serial is connected
                # if 'teensy' in locals():
                #     teensy.write('*1,{}\n'.format(repr(visual_queue)).encode('Ascii'))

            text = text_label + " (" + str(round(visual_queue,2)) + ")"

            handler.draw_box(image)
            handler.put_text(image, text)

        # To improve performance, optionally mark the image as not writeable to pass by reference.
        image.flags.writeable = False

        # Display the resulting frame
        cv2.imshow('MediaPipe Gesture Recognition', image)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release the video capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()