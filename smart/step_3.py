#!/usr/bin/env python


import time
from threading import Thread
import sub_2
import rospy
import serial



SUB = sub_2.Sub()

class StepMotor:
    def __init__(self, Dir):        
        step = 1

        self.dir = Dir
        if self.dir == 1:
            self.way = "E"
        elif self.dir == 2:
            self.way = "N"
        else:
            self.way = "No"
       
        
        print("----------StepMotor----------")
        
        if self.way == "E":
            if SUB.listener_buttonL() == 1:
                print("-----buttonL is connected!-----")
            else:
                print("-----buttonL is not connected!-----")
        
        elif self.way == "N":
            if SUB.listener_buttonR() == 1:
                print("-----buttonR is connected!-----")
            else:
                print("-----buttonR is not connected!-----")
            
        
        thread = Thread(target=self.run, args=(self.way,))
        thread.daemon = True
        thread.start()
        
        
    def run(self, a):
        print("-----run Thread %s!-----" %a)
            
        
        while True:
            if a == "E":
                step = SUB.listener_buttonL()
            elif a == "N":
                step = SUB.listener_buttonR()

            step = int(step)
            #speed = (int(speed) - 50)*2
            
            ser.write(str.encode(a + str(step)))
            print("step"+a+":"+(str(step)))
            #time.sleep(1)
            
            if step == 2 or step == 1 or step == 0:
                ser.write(str.encode(a + str(step)))
                
            else:
                ser.write(str.encode(a + str(1)))
                
                
                
                
                
                
                
                
                
                
                
                
                