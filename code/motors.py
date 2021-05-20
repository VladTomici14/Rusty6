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

for i in range(8):
    GPIO.setup(motors[i], GPIO.OUT)
    GPIO.output(motors[i], GPIO.LOW)

def move(motor):
    GPIO.output(motor, GPIO.HIGH)
    time.sleep(3)
    GPIO.output(motor, GPIO.LOW)

if __name__ == "__main__":
    while(True):
        command = str(input("choose a motor: "))

        if charge_mode == False:

        if command == "forward1":
            move(forward1)

        elif command == "backward1":
            move(backward1)

        elif command == "forward2":
            move(forward2)

        elif command == "backward2":
            move(backward2)

        elif command == "forward3":
            move(forward3)

        elif command == "backward3":
            move(backward3)

        elif command == "forward4":
            move(forward4)

        elif command == "backward4":
            move(backward4)

        elif command == "exit":
            break

        else:
            print("sorry, please enter a valid command")