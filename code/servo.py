import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

servo1 = 4
servo2 = 5

GPIO.setup(servo1, GPIO.OUT)
pwm = GPIO.PWM(servo1, 50)

pwm.start(0)

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