#!/usr/bin/env python
import rospy
from sensor_msgs.msg import CompressedImage
from std_msgs.msg import String

def publish_image(image_data):
    pub = rospy.Publisher('/camera/image/compressed', CompressedImage, queue_size=10)
    image_msg = CompressedImage()
    image_msg.format = "jpeg"
    image_msg.header.stamp = rospy.Time.now()
    image_msg.data = image_data
    pub.publish(image_msg)

def publish_info(info1, info2):
    pub1 = rospy.Publisher('/info1', String, queue_size=10)
    pub2 = rospy.Publisher('/info2', String, queue_size=10)
    info_msg1 = String()
    info_msg1.data = info1
    pub1.publish(info_msg1)
    info_msg2 = String()
    info_msg2.data = info2
    pub2.publish(info_msg2)

if __name__ == '__main__':
    rospy.init_node('image_info_publisher', anonymous=True)
    image_data = b'YOUR_IMAGE_DATA' # Replace with your image data
    publish_image(image_data)
    info1 = 'INFO1' # Replace with your information
    info2 = 'INFO2' # Replace with your information
    publish_info(info1, info2)
    rospy.spin()
    
