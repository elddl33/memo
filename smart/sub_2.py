#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from std_msgs.msg import Int32
import time
import serial


class Sub:
    def __init__(self):
        #self.ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
        self.msg_data_seekBarL = 50
        self.msg_data_seekBarR = 50
        self.msg_data_buttonL = 1
        self.msg_data_buttonR = 1
        rospy.Subscriber('/seekBarL', Int32, self.callback_seekBarL)
        rospy.Subscriber('/seekBarR', Int32, self.callback_seekBarR)
        rospy.Subscriber('/buttonL', Int32, self.callback_buttonL)
        rospy.Subscriber('/buttonR', Int32, self.callback_buttonR)
        
        
        
    def callback_seekBarL(self, msg):
        self.msg_data_seekBarL = msg.data
        
    def callback_seekBarR(self, msg):
        self.msg_data_seekBarR = msg.data
        
    def callback_buttonL(self, msg):
        self.msg_data_buttonL = msg.data
        
    def callback_buttonR(self, msg):
        self.msg_data_buttonR = msg.data



    def listener_seekBarL(self):
        return self.msg_data_seekBarL
    
    
    def listener_seekBarR(self):
        return self.msg_data_seekBarR

        
    def listener_buttonL(self):
        return self.msg_data_buttonL

        
    def listener_buttonR(self):
        return self.msg_data_buttonR


    
    



    
#if __name__ == '__main__':
#    rospy.init_node('Control_listener', anonymous=True)
##    rate = rospy.Rate(10) # 10 Hz
#    while not rospy.is_shutdown():
#        listener_1()
#        listener_2()
#        listener_3()
#        listener_4()
#        rate.sleep()

