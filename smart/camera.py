#!/usr/bin/env python

from flask import Flask, render_template, Response
from threading import Thread
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

from flask import Flask, render_template, Response
from threading import Thread
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

app = Flask(__name__)
bridge = CvBridge()
#pub = rospy.Publisher("camera/image", Image, queue_size=10)
image = None

class Camera:
    def __init__(self, cam_num):
        global image
        self.cap = cv2.VideoCapture(cam_num)
        self.frame = None
        rate = rospy. Rate(10) # 10 Hz
        print("-------RGB_Camera-------")
        print("RGB_Camera", cam_num)
        
    def start(self):
        thread = Thread(target=self.gen_frame, args=())
        thread.daemon = True
        thread.start()
        
    def gen_frame(self):
        while True:
            ret, frame = self.cap.read()
            if not ret:
                print("RGB_Cam is shutdown")
                break
            if cv2.waitKey(1) == ord('q'):
                break
            cv2.imshow('USB Camera', frame)
            frame = cv2.resize(frame, (1440, 870))
            ret, jpeg = cv2.imencode(".jpg", frame)
            frame = jpeg.tobytes() # Convert to byte array
            yield (b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n\r\n")
            