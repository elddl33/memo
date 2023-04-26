#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import serial

def info_publisher():
    # node reset
    rospy.init_node('info_publisher', anonymous=True)
    
    #topic pub
    pub = rospy.Publisher('/info', String, queue_size=10)


    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        # topic input
        info = raw_input('Enter information: ')

        # topic send
        pub.publish(info)

        rate.sleep()

if __name__ == '__main__':
    try:
        info_publisher()
    except rospy.ROSInterruptException:
        pass
