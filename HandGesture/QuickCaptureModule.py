import cv2
import threading
import queue

class Capture:
    def __init__(self, src=0):
        self.cap = cv2.VideoCapture(src)
        self.cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
        #self.width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        #self.height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

        self.q = queue.Queue()
        self.t = threading.Thread(target=self._reader)
        self.t.daemon = True
        self.t.start()
        #self.timestamp_ms = int(self.cap.get(cv2.CAP_PROP_POS_MSEC))

    def _reader(self):
        while True:
            ret, frame = self.cap.read()
            self.timestamp_ms = int(self.cap.get(cv2.CAP_PROP_POS_MSEC))

            if not ret:
                break
            if not self.q.empty():
                try:
                    self.q.get_nowait()  # Discard previous (unprocessed) frame
                except queue.Empty:
                    pass
            self.q.put(frame)

    def read(self):
        return self.q.get()
    
    def size(self):
        return int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    def isOpened(self):
        return self.cap.isOpened()
    
    #def get_timestamp_ms(self):
    #    return self.timestamp_ms

    def release(self):
        self.cap.release()