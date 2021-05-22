import RPi.GPIO as GPIO
import time
import argparse

GPIO.setwarnings(False)

ap = argparse.ArgumentParser()
ap.add_argument("-s", "--state", type = str, required = True)
args = ap.parse_args()

GPIO.setmode(GPIO.BCM)
SOLAR = 8
GPIO.setup(SOLAR, GPIO.OUT)

if args.state == "yes":
    GPIO.output(SOLAR, GPIO.HIGH)

elif args.state == "no":
    GPIO.output(SOLAR, GPIO.LOW)

else:
    GPIO.output(SOLAR, GPIO.LOW)