"""
------------------------------------------------------------------------------------------------------------------------
Remote Light_switch Server
By Jesse Leventhal
11/24/18
v 1.0.0

This is a small flask server for a Raspberry Pi (or other single board computers).
Controls a micro servo which can turn on and off a paddle style light switch.

See Thingiverse.com post for the micro servo switch plate mount.

Make sure to adjust your on/off angles to the fit your lightswitch.

!!!!CHANGE ALL IP ADDRESSES IN APP.PY AND INDEX.HTML TO YOUR PI'S IP ADDRESS!!!!
------------------------------------------------------------------------------------------------------------------------
"""

from flask import Flask, render_template, redirect
import RPi.GPIO as GPIO
from time import sleep

serv_pin = 4 #signal pin for servo

#Use the test.py file to determine the correct angle to turn the switch on and off
servo_on_angle = 110
servo_off_angle = 65

"""
Function setup----------------------------------------------------------------------------------------------------------
"""


def SetAngle(angle):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(serv_pin, GPIO.OUT)
    pwm = GPIO.PWM(serv_pin, 50)
    pwm.start(0)
    GPIO.setwarnings(False)

    duty = angle / 18 + 2
    GPIO.output(serv_pin, True)
    pwm.ChangeDutyCycle(duty)
    sleep(0.5)
    GPIO.output(serv_pin, False)
    pwm.ChangeDutyCycle(0)
    pwm.stop()
    GPIO.cleanup()


def light_on():
    SetAngle(servo_on_angle)
    sleep(0.5)
    SetAngle(90)


def light_off():
    SetAngle(servo_off_angle)
    sleep(0.5)
    SetAngle(90)


"""
Flask setup-------------------------------------------------------------------------------------------------------------
"""

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/mainlight/<switch_state>')
def switch_func(switch_state):
    if switch_state == 'on':
        light_on()
    elif switch_state == 'off':
        light_off()
    else:
        return ('Unknown light State', 400)

    return redirect("http://192.168.0.33:5000/") # Put your Pi's IP address here


if __name__ == '__main__': #todo: Optimize speed of and reliablity of server
    app.run(debug=False, host='0.0.0.0', threaded=True)

