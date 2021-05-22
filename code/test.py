import RPi.GPIO as GPIO
import time

#GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

motors = 25
solar = 8
GPIO.setup(motors, GPIO.OUT)
GPIO.setup(solar, GPIO.OUT)

time.sleep(2)
print("something")

GPIO.cleanup()