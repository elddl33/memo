#!/usr/bin/env python


#import Jetson.GPIO as GPIO
import time
from threading import Thread
import sub_2
import rospy
import serial
#GPIO.setmode(GPIO.BOARD)

#sub
SUB = sub_2.Sub()

class Motor:
    def __init__(self, Dir):
        self.ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
        self.ser.flushInput()
        speed = 0

        self.dir = Dir
        if self.dir == 1:
            self.way = "L"
        elif self.dir == 2:
            self.way = "R"
        else:
            self.way = "No"
       
        
        print("----------Motor----------")
        
        if self.way == "L":
            if SUB.listener_seekBarL() == 50:
                print("-----seekBarL is connected!-----")
            else:
                print("-----seekBarL is not connected!-----")
        
        elif self.way == "R":
            if SUB.listener_seekBarR() == 50:
                print("-----seekBarR is connected!-----")
            else:
                print("-----seekBarR is not connected!-----")
            
        
        thread = Thread(target=self.run, args=(self.way,))
        thread.daemon = True
        thread.start()
        
        
        
    def run(self, a):
        print("-----run Thread %s!-----" %a)
            
        
        while True:
            if a == "L":
                speed = SUB.listener_seekBarL()
            elif a == "R":
                speed = SUB.listener_seekBarR()

            speed = int(speed)
            #speed = (int(speed) - 50)*2
            
            ser.write(str.encode(a + str(speed)))
            #print("motor"+a+":"+(str(speed)))
            time.sleep(0.1)
            
            if speed == 0:                
                ser.write(str.encode(a + str(speed)))

            elif speed < 0:
                ser.write(str.encode(a + str(speed)))
                    
            elif speed > 0:
                ser.write(str.encode(a + str(speed)))
                    
            
    


