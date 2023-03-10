#!/usr/bin/env python

import Jetson.GPIO as GPIO
import time

LED_PIN = 32


GPIO.setmode(GPIO.BOARD)


GPIO.setup(LED_PIN, GPIO.OUT)


pwm = GPIO.PWM(LED_PIN, 1000)


pwm.start(0)

try:
    while True:

        for dc in range(0, 101, 5):
            pwm.ChangeDutyCycle(dc)
            time.sleep(0.1)
        
        for dc in range(100, -1, -5):
            pwm.ChangeDutyCycle(dc)
            time.sleep(0.1)
            
except KeyboardInterrupt:

    pwm.stop()
    GPIO.cleanup()