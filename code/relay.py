import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

relay = 25
GPIO.setup(relay, GPIO.OUT)
GPIO.output(relay, GPIO.LOW)
time.sleep(2)
GPIO.output(relay, GPIO.HIGH)
time.sleep(2)
GPIO.output(relay, GPIO.LOW)

GPIO.setwarnings(False)