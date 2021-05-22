import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

relay = 12
GPIO.setup(relay, GPIO.OUT)
GPIO.output(relay, GPIO.LOW)
time.sleep(2)
GPIO.output(relay, GPIO.HIGH)

GPIO.setwarnings(False)