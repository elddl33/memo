#!/usr/bin/env python


import Jetson.GPIO as GPIO
import time
from threading import Thread
GPIO.setmode(GPIO.BOARD)


class Motor:
    def __init__(self, EN, INA, INB = None):
        self.ina = INA
        self.inb = INB
        if (self.inb != None):
            GPIO.setup(self.inb, GPIO.OUT)
        
        GPIO.setup(EN, GPIO.OUT)
        GPIO.setup(INA, GPIO.OUT)
        
        
        
        print("----------Motor----------")
        print("PWM: ", self.pwm)
        print("INA: ", self.ina)
        print("INB: ", self.inb)
        
    def start(self):
        thread = Thread(target=self.motor_speed, args=())
        thread.daemon = True
        thread.start()
        return self
        

    def motor_speed(self, speed):
        
        while True:
            self.pwm = abs(speed)
            self.ontime = self.pwm
            self.offtime = 100 - self.pwm
            
            if speed == 0:
                GPIO.output(self.ina, 0)
                
                if(self.inb != None):
                    GPIO.output(self.inb, 0)

            elif speed < 0:
                GPIO.output(self.ina, 0)

                if(self.inb != None):
                    print("ff")
                    GPIO.output(self.inb, 1)
                    
            elif speed > 0:
                GPIO.output(self.ina, 1)
                
                if(self.inb != None):
                    GPIO.output(self.inb, 0)
                    
            GPIO.output(EN, GPIO.HIGH)
            time.sleep(self.ontime/1000)
            GPIO.output(EN, GPIO.LOW)
            time.sleep(self.offtime/1000)

#obj = Motor(26,19,20)
#obj.motor_speed(33)
#time.sleep(5)
#obj.motor_speed(0)
#time.sleep(3)
#obj.motor_speed(-33)
#time.sleep(5)
#GPIO.cleanup()
