#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)

def listener_1():
    rospy.Subscriber('/seekBarL', String, callback)

    
    
def listener_2():
    rospy.Subscriber('/seekBarR', String, callback)

    
    
def listener_3():
    rospy.Subscriber('/buttonL', String, callback)

    
    
def listener_4():
    rospy.Subscriber('/buttonR', String, callback)


    
if __name__ == '__main__':
    rospy.init_node('Control_listener', anonymous=True)
    rate = rospy.Rate(10) # 10 Hz
    while not rospy.is_shutdown():
        listener_1()
        listener_2()
        listener_3()
        listener_4()
        rate.sleep()

