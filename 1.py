#!/usr/bin/env python

import Jetson.GPIO as GPIO
import time

LED_PIN = 33


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(LED_PIN, GPIO.OUT)


#pwm = GPIO.PWM(LED_PIN, 1000)


#pwm.start(0)



try:
    while True:
        
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(0.00000001)
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(0.0001)

            
except KeyboardInterrupt:

    pwm.stop()
    GPIO.cleanup()
