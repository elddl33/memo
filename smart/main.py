#!/usr/bin/env python

from flask import Flask, render_template, session, request, Response
from threading import Thread
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
#import motor2
import motor4
import step_3
import camera
#import gas_sensor
#import DHT11
#import webcam_ORG
import time
import pub_2
import sub_2
import sonic_2
import serial
time.sleep(3)

#gassensor
#SPICLK = 11
#SPIMISO = 9
#SPIMOSI = 10
#SPICS = 19
#mq2_dpin = 26
#mq2_apin = 0


# Flask_server
app = Flask(__name__)
bridge = CvBridge()

#gas = gas_sensor.GasSensor(SPICLK, SPIMISO, SPIMOSI, SPICS, mq2_dpin, mq2_apin)
rospy.init_node('listener', anonymous=True)

#serial port
#ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)#/dev/ttyACM0  sudo chmod a+rw /dev/ttyACM0
#if already using port = sudo chmod 666 /dev/ttyACM0 

#motor
motors = []
#motors = motor2.Motor(33,23)
#motors.append((motor4.Motor(1), motor4.Motor(2))) ##1 = L, 2 = R
#motors.append((motor2.Motor(27,22), motor2.Motor(5,6)))

#stepMotor
steps = []
#steps.append((step_3.StepMotor(1), step_3.StepMotor(2))) ##1 = L, 2 = R

#camera
cameras = []
cameras.append(camera.Camera(0).start()) ##RGB_Cam
#cameras.append(webcam_ORG.DetectCam(1, 12).start()) ##Thermal_Cam

#sonics = []
#sonics.append(sonic_2.Sonic(22,21))




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

#rospy.init_node('listener', anonymous=True)
#SUB_1 = sub.Sub()
#speed = SUB_1.listener()
#speed = (int(speed) - 50)*2



print("--------------------------")



#while not rospy.is_shutdown():
#    speed = SUB_1.listener()
#    speed = (int(speed) - 50)*2
#    if speed != 0:
#        mymotor(0, speed)
#        rospy.loginfo("speed : %s", speed)
#motors[0]
#steps[0]
#sonics[0]



@app.route("/")
def index():                            
    return render_template("index.html") # Render the web page template

#RGB_camera
@app.route('/RGB_video_feed')
def RGB_video_feed():
    return Response(camera.Camera(0).gen_frame(), mimetype="multipart/x-mixed-replace; boundary=frame") # video stream response

#Fire_camera
#@app.route('/Fire')
#def Fire_video_feed():
#    return Response(generate(), mimetype="multipart/x-mixed-replace; boundary=frame") # video stream response




if __name__ == '__main__':
    try:
        app.run(host="192.168.0.141", port=8080, debug=True) # Run flask application        
            
    except:
        #GPIO.cleanup()
        ser.close() # Close the serial port