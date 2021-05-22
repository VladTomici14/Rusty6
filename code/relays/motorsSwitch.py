import RPi.GPIO as GPIO
import time
import argparse

GPIO.setwarnings(False)

ap = argparse.ArgumentParser()
ap.add_argument("-s", "--state", type = str, required = True)
args = ap.parse_args()

GPIO.setmode(GPIO.BCM)
MOTOR = 25
GPIO.setup(MOTOR, GPIO.OUT)

if args.state == "yes":
    GPIO.output(MOTOR, GPIO.HIGH)

elif args.state == "no":
    GPIO.output(MOTOR, GPIO.LOW)
    GPIO.cleanup()

else:
    GPIO.output(MOTOR, GPIO.LOW)