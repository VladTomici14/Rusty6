import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)  # GPIO Numbers instead of board numbers

RELAIS_1_GPIO = 25
GPIO.setup(RELAIS_1_GPIO, GPIO.OUT)  # GPIO Assign mode
GPIO.output(RELAIS_1_GPIO, GPIO.LOW)  # out
GPIO.output(RELAIS_1_GPIO, GPIO.HIGH)  # on
GPIO.output(RELAIS_1_GPIO, GPIO.LOW)  # out

GPIO.cleanup()