#!/usr/bin/env python

import motor2
#import camera
#import gas_sensor
#import DHT11
import Jetson.GPIO as GPIO
#import RPi.GPIO as GPIO
from threading import Thread
#import webcam_ORG
import time
import cv2
import rospy
import pub_2
import sub
import sub_2
time.sleep(5)
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
#startpin = 12
#GPIO.setup(startpin, GPIO.OUT)

#gassensor
#SPICLK = 11
#SPIMISO = 9
#SPIMOSI = 10
#SPICS = 19
#mq2_dpin = 26
#mq2_apin = 0

#gas = gas_sensor.GasSensor(SPICLK, SPIMISO, SPIMOSI, SPICS, mq2_dpin, mq2_apin)

#motor
motors = []
#motors = motor2.Motor(33,23)
motors.append((motor2.Motor(33, 23))) #, motor2.Motor(32,11)))
#motors.append((motor2.Motor(27,22), motor2.Motor(5,6)))



#camera
#cameras = []
#cameras.append(webcam_ORG.DetectCam(2, 12).start())
#cameras.append(camera.Camera(4, 12).start())
#cameras.append(camera.Camera(0, 12).start())

#dht11
#dht11 = []
#dht11.append(DHT11.DHT11Sensor(26))
#dht11.append(DHT11.DHT11Sensor(20))

#sub
rospy.init_node('listener', anonymous=True)
SUB_1 = sub.Sub()
speed = SUB_1.listener()
speed = (int(speed) - 50)*2



print("--------------------------")
#@app.route('/')
#def main():
#    return render_template('index.html')

#@app.route('/start')
#def mystart():
#    try:
#        thread4 = Thread(target=radar1.move_radar, args=())
#        thread4.daemon = True
#        thread4.start()
#        print("Thread4_Start.. done") 
#        return "ok"
#    except:
#        return "fail"

#camera
#@app.route('/video_feed/<num>/<state>')
#def video_feed(num, state):
#    num = int(num)
#    if(int(state) == 1):
#        cameras[num].set_state(True)
#        cameras[num].clear_q()
#        return Response( cameras[num].get_q() , mimetype='multipart/x-mixed-replace; boundary=frame')
#    cameras[num].set_state(False)
#    return Response( cameras[num].loading() , mimetype='multipart/x-mixed-replace; boundary=frame')

#motor
#@app.route('/motor/<num>/<speed>')
#def mymoter(num, speed):
#    try:
#        print("Motor", num, ": ", speed)
#        if ( type(motors[int(num)]) != type(()) ):
#            motors[int(num)].motor_speed(int(speed))
#        else:
#            motors[int(num)][0].motor_speed(int(speed))
#            motors[int(num)][1].motor_speed(int(speed))
#        return speed
#    except:
#        return "fail"

def mymotor(num, speed):
    try:
        print("Motor", num, ": ", speed)
        if ( type(motors[int(num)]) != type(()) ):
            motors[int(num)].motor_speed(int(speed))
        else:
            motors[int(num)][0].motor_speed(int(speed))
            motors[int(num)][1].motor_speed(int(speed))
        return speed
    except:
        return "fail"


while not rospy.is_shutdown():
    speed = SUB_1.listener()
    speed = (int(speed) - 50)*2
    if speed != 0:
        mymotor(0, speed)
        rospy.loginfo("speed : %s", speed)
#gas
#@app.route('/gas')
#def mygas():
#    try:
#        return str(gas.readadc())
#    except:
#        return "fail"
    
#DHT11
#@app.route('/DHT11/<num>')
#def myDHT11(num):
#    try:
#        return str(dht11[int(num)].readtemp())
#    except:
#        return "fail"




if __name__ == '__main__':
    try:
        GPIO.output(startpin, True)
        #app.run(host='0.0.0.0', port=8080)#, debug=True)
        GPIO.output(startpin, False)
    except:
        GPIO.cleanup()
        