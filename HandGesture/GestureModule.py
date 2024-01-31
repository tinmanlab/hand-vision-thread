# Reference : https://developers.google.com/mediapipe/solutions/vision/gesture_recognizer

import cv2
import mediapipe as mp
import time

class GestureHandler:
    def __init__(self, cap):
        self.g_min_x = 0
        self.g_min_y = 0
        self.g_max_x = 0
        self.g_max_y = 0
        self.detect = False
        self.label = None
        self.score = 0
        self.prev_time = time.time()
        self.width, self.height = cap.size()

        #self.cap = cap

    def print_result(self, result: mp.tasks.vision.GestureRecognizerResult, *_):
        max_x = 0
        min_x = 1
        max_y = 0
        min_y = 1

        self.detect = False

        for hand in result.hand_landmarks:
            for landmark in hand:
                if landmark.x > max_x:
                    max_x = landmark.x
                if landmark.x < min_x:
                    min_x = landmark.x

                if landmark.y > max_y:
                    max_y = landmark.y
                if landmark.y < min_y:
                    min_y = landmark.y
            
            self.detect = True

            self.g_min_x, self.g_max_x = min_x * self.width, max_x * self.width
            self.g_min_y, self.g_max_y = min_y * self.height, max_y * self.height
            
        for gesture_list in result.gestures:
            for gesture in gesture_list:
                self.label = gesture.category_name
                self.score = gesture.score

    def is_detected(self):
        return self.detect

    def get_box(self):
        return self.g_min_x, self.g_min_y, self.g_max_x, self.g_max_y
    
    def get_label(self):
        return self.label
    
    def get_score(self):
        return self.score
    
    def is_cap_size_over(self, width=320, height=240):
        if self.width >= 320 & self.height >= 240:
            return True
        else:
            return False 

    def get_frame(self, image):
        curr_time = time.time()
        frame_rate = 1 / (curr_time - self.prev_time)
        self.prev_time = curr_time

        if self.is_cap_size_over(320,240):
            cv2.putText(image, str(round(frame_rate,2)) + " FPS", (5, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)       
    
    def draw_box(self, image):
        cv2.rectangle(image, (int(self.g_min_x-15), int(self.g_min_y-15)), (int(self.g_max_x+15), int(self.g_max_y+15)), (0, 255, 0), 2)

    def put_text(self, image, text):
        if self.is_cap_size_over(320,240):
            cv2.putText(image, text, (int(self.g_min_x), int(self.g_min_y-25)), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
        else:
            print(text)