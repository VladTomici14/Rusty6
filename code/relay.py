import RPi.GPIO as GPIO
import time

def motorsOn():
    GPIO.setup(relay, GPIO.OUT)


def motorsOff():
    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)

GPIO.setmode(GPIO.BCM)

relay = 25
k = 0

try:
    while True:
        command = str(input("command: "))
        if command == "k":
            k = k + 1
        elif command == "q":
            break

        if k % 2 == False:
            motorsOff()
        else:
            motorsOn()

except KeyboardInterrupt:
    print("keyboard interrupt")

except:
    print("some error")

finally:
    GPIO.cleanup()