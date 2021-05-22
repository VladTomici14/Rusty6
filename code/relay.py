import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

MOTORS = 25
SOLAR = 8

GPIO.setup(MOTORS, GPIO.OUT)
GPIO.output(MOTORS, GPIO.LOW)

command = str(input(""))


time.sleep(3)

GPIO.cleanup()