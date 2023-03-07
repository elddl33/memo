#!/usr/bin/env python

import rospy
from std_msgs.msg import String
#int_data = 0


class Sub:
    def __init__(self):
        #rospy.init_node('listener', anonymous=True)
        self.msg_data = 50
        self.sub = rospy.Subscriber('/seekBarR', String, self.callback)
    
    def callback(self, msg):
        self.msg_data = msg.data

    def listener(self):
        return self.msg_data


