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

def initializeMotors():
    for i in range(8):
        GPIO.setup(motors[i], GPIO.OUT)
        GPIO.output(motors[i], False)

def move(motor):
    GPIO.output(motor, True)
    time.sleep(3)
    GPIO.output(motor, False)

if __name__ == "__main__":
    try:
        while True:
            GPIO.cleanup()
            command = str(input("command: "))
            if command == "motorson":
                GPIO.cleanup()
                time.sleep(0.3)
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(motorsSwitch, GPIO.OUT)

            elif command == "motorsoff":
                GPIO.cleanup()

            elif command == "solaron":
                GPIO.cleanup()
                time.sleep(0.3)
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(solarSwitch, GPIO.OUT)

            elif command == "solaroff":
                GPIO.cleanup()

            if command == "forward1":
                initializeMotors()
                move(forward1)
                move(forward2)
                move(forward3)
                move(forward4)

            elif command == "backward":
                initializeMotors()
                move(backward1)
                move(backward2)
                move(backward3)
                move(backward4)

            if command == "exit":
                break
                GPIO.cleanup()

    except KeyboardInterrupt:
        GPIO.cleanup()

    GPIO.cleaupt()