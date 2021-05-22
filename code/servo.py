import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

servo1 = 4
servo2 = 5

pwm = GPIO.PWM(servo1, 50)


def setAngle(angle):
    duty = angle / 18 + 2
    GPIO.output(servo1, GPIO.HIGH)
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)
    GPIO.output(servo1, GPIO.LOW)
    pwm.ChangeDutyCycle(0)

setAngle(30)
pwm.stop()
GPIO.cleanup()