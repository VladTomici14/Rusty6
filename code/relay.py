import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

MOTORS = 25
SOLAR = 8

GPIO.setup(MOTORS, GPIO.OUT)
GPIO.output(MOTORS, GPIO.LOW)

GPIO.setup(SOLAR, GPIO.OUT)
GPIO.output(SOLAR, GPIO.LOW)

command = str(input(""))
if command == "motorson":
    GPIO.output(SOLAR, GPIO.LOW)
    time.sleep(0.3)
    GPIO.output(MOTORS, GPIO.HIGH)

elif command == "motorsoff":
    GPIO.output(MOTORS, GPIO.LOW)

elif command == "solaron":
    GPIO.output(MOTORS, GPIO.LOW)
    time.sleep(0.3)
    GPIO.output(SOLAR, GPIO.HIGH)

elif command == "solaroff":
    GPIO.output(SOLAR, GPIO.LOW)


time.sleep(3)

GPIO.cleanup()