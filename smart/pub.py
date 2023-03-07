#!/usr/bin/env python

import rospy
from sensor_msgs.msg import CompressedImage
from std_msgs.msg import String
import cv2
import numpy as np


def image_publisher(image_path):
    pub = rospy.Publisher('/camera/image/compressed', CompressedImage, queue_size=10)
    image_msg = CompressedImage()
    image_msg.format = "jpeg"
    image_msg.header.stamp = rospy.Time.now()
    
    with open(image_path, 'rb') as f:
        image_data = f.read()

    image_msg.data = image_data
    print(image_data)
    pub.publish(image_msg)
    

def info1_publisher(info1):
    pub = rospy.Publisher('/info1', String, queue_size=10)
    info_msg = String()
    info_msg.data = info1
    pub.publish(info_msg)


def info2_publisher(info2):
    pub = rospy.Publisher('/info2', String, queue_size=10)
    info_msg = String()
    info_msg.data = info2
    pub.publish(info_msg)



if __name__ == '__main__':
    rospy.init_node('multiple_publishers', anonymous=True)
    image_path = '/home/khw/catkin_ws/src/smart/images/image.jpg'
    info1 = 'INFO1' # Replace with your information
    info2 = 'INFO2' # Replace with your information
    rate = rospy.Rate(10) # 10 Hz
    while not rospy.is_shutdown():
        image_publisher(image_path)
        rospy.sleep(0.1) # wait for the image publisher to finish publishing
        info1_publisher(info1)
        info2_publisher(info2)
        rate.sleep()
        