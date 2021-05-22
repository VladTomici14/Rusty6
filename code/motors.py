import RPi.GPIO as GPIO
import time

motors = []
GPIO.setmode(GPIO.BCM)

forward1 = 21
backward1 = 20
motors.append(forward1)
motors.append(backward1)

forward2 = 16
backward2 = 26
motors.append(forward2)
motors.append(backward2)

forward3 = 19
backward3 = 13
motors.append(forward3)
motors.append(backward3)

forward4 = 6
backward4 = 5
motors.append(forward4)
motors.append(backward4)

modes = ["easy", "medium", "high"]
charge_mode = False

motorsSwitch = 25
solarSwitch = 8

GPIO.setup(motors, GPIO.OUT)

def move(motor):
    GPIO.output(motor, True)
    time.sleep(3)
    GPIO.output(motor, False)

if __name__ == "__main__":
    try:
        while True:
            command = str(input("command: "))

            if command == "forward1":
                move(forward1)
                move(forward2)
                move(forward3)
                move(forward4)

            elif command == "backward":
                move(backward1)
                move(backward2)
                move(backward3)
                move(backward4)

            if command == "exit":
                break
                GPIO.cleanup()

    except KeyboardInterrupt:
        GPIO.cleanup()

    GPIO.cleaup()