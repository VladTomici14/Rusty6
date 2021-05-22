import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

relay = 25
GPIO.setup(relay, GPIO.OUT)
GPIO.output(relay, False)

k = 0
while True:
    command = str(input("command: "))
    if command == "k":
        k = k + 1
    elif command == "q":
        break

    if k % 2 == False:
        GPIO.output(relay, False)
    else:
       GPIO.output(relay, True)

finally:
    GPIO.cleanup()