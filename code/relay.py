import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

relay = 22
GPIO.setup(relay, GPIO.OUT)

GPIO.output(relay, False)
print("false")

time.sleep(2)

GPIO.output(relay, True)
print("true")

time.sleep(2)

GPIO.output(relay, False)
print("false")
