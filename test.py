import RPi.GPIO as GPIO
from time import sleep


def SetAngle(angle):
    sPin = 4

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(sPin, GPIO.OUT)
    pwm = GPIO.PWM(sPin, 50)
    pwm.start(0)
    GPIO.setwarnings(False)

    duty = angle / 18 + 2
    GPIO.output(sPin, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(sPin, False)
    pwm.ChangeDutyCycle(0)
    pwm.stop()
    GPIO.cleanup()



def switch_on():
    SetAngle(110)
    sleep(1)
    SetAngle(90)

def switch_off():
    SetAngle(65)
    sleep(1)
    SetAngle(90)