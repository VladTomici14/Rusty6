import RPi.GPIO as GPIO
import time
from . import powerFunctions

motors = []
GPIO.setmode("GPIO.BCM")

forward1 =
backward1 =
motors.append(forward1)
motors.append(backward1)

forward2 =
backward2 =
motors.append(forward2)
motors.append(backward2)

forward3 =
backward3 =
motors.append(forward3)
motors.append(backward3)

forward4 =
backward4 =
motors.append(forward4)
motors.append(backward4)

modes = ["easy", "medium", "high"]

for i in range(8):
    GPIO.setup(motors[i], GPIO.OUT)
    GPIO.output(motors[i], GPIO.LOW)


if __name__ == "__main__":
    selectedMode = str(input("choose a mode: "))
    if selectedMode == modes[0]:
        intensity = 30

    elif selectedMode == modes[1]:
        intensity = 60

    elif selectedMode == modes[2]:
        intensity = 100


