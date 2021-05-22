import RPi.GPIO as GPIO
import time

motors = 22
solar = 24

GPIO.setmode(GPIO.BOARD)
GPIO.setup(motors, GPIO.OUT)
GPIO.setup(solar, GPIO.OUT)

try:
    while True:
        for x in range(5):
            GPIO.output(motors, True)
            time.sleep(0.1)
            GPIO.output(motors, False)
            GPIO.output(solar, True)
            time.sleep(0.1)
            GPIO.output(solar, False)

        GPIO.output(motors,True)
        GPIO.output(solar,True)

except KeyboardInterrupt:
    GPIO.cleanup()