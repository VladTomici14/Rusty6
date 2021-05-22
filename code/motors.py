import RPi.GPIO as GPIO
import time
import curses
import cv2
import picamera
import os
from random import randint

faceCascadePath = "../haarcascades/"
faceCascade = cv2.CascadeClassifier(faceCascadePath)

upperBodyCascadePath = "../haarcascades/"
upperBodyCascade = cv2.CascadeClassifier(upperBodyCascadePath)

lowerBodyCascadePath = ""
lowerBodyCascade = cv2.CascadeClassifier(lowerBodyCascadePath)

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

motors = []
GPIO.setmode(GPIO.BCM)

forward1 = 12
backward1 = 24
motors.append(forward1)
motors.append(backward1)

forward2 = 23
backward2 = 18
motors.append(forward2)
motors.append(backward2)

forward3 = 26
backward3 = 13
motors.append(forward3)
motors.append(backward3)

forward4 = 5
backward4 = 6
motors.append(forward4)
motors.append(backward4)

modes = ["easy", "medium", "high"]

GPIO.setup(motors, GPIO.OUT)
for i in range(len(motors)):
    GPIO.output(motors[i], GPIO.LOW)

# here we will define some functions

# moves Rusty forward
def forward():
    GPIO.output(forward1, GPIO.HIGH)
    GPIO.output(backward1, GPIO.LOW)

    GPIO.output(forward2, GPIO.HIGH)
    GPIO.output(backward2, GPIO.LOW)

    GPIO.output(forward3, GPIO.HIGH)
    GPIO.output(backward3, GPIO.LOW)

    GPIO.output(forward4, GPIO.HIGH)
    GPIO.output(backward4, GPIO.LOW)
    time.sleep(0.1)
    for i in range(len(motors)):
        GPIO.output(motors[i], GPIO.LOW)

# moves Rusty backward
def backward():
    GPIO.output(forward1, GPIO.LOW)
    GPIO.output(backward1, GPIO.HIGH)

    GPIO.output(forward2, GPIO.LOW)
    GPIO.output(backward2, GPIO.HIGH)

    GPIO.output(forward3, GPIO.LOW)
    GPIO.output(backward3, GPIO.HIGH)

    GPIO.output(forward4, GPIO.LOW)
    GPIO.output(backward4, GPIO.HIGH)
    time.sleep(0.1)
    for i in range(len(motors)):
        GPIO.output(motors[i], GPIO.LOW)

# move Rusty to the right
def right():
    GPIO.output(forward1, GPIO.HIGH)
    GPIO.output(backward1, GPIO.LOW)

    GPIO.output(forward2, GPIO.LOW)
    GPIO.output(backward2, GPIO.HIGH)

    GPIO.output(forward3, GPIO.LOW)
    GPIO.output(backward3, GPIO.HIGH)

    GPIO.output(forward4, GPIO.HIGH)
    GPIO.output(backward4, GPIO.LOW)
    time.sleep(0.1)
    for i in range(len(motors)):
        GPIO.output(motors[i], GPIO.LOW)

# moves Rusty to the left
def left():
    GPIO.output(forward1, GPIO.LOW)
    GPIO.output(backward1, GPIO.HIGH)

    GPIO.output(forward2, GPIO.HIGH)
    GPIO.output(backward2, GPIO.LOW)

    GPIO.output(forward3, GPIO.HIGH)
    GPIO.output(backward3, GPIO.LOW)

    GPIO.output(forward4, GPIO.LOW)
    GPIO.output(backward4, GPIO.HIGH)
    time.sleep(0.1)
    for i in range(len(motors)):
        GPIO.output(motors[i], GPIO.LOW)

if __name__ == "__main__":
    try:
        while True:
            char = screen.getch()

            if char == ord("w") or char == curses.KEY_UP:
                forward()
            elif char == ord("a") or char == curses.KEY_LEFT:
                left()
            elif char == ord("s") or char == curses.KEY_DOWN:
                backward()
            elif char == ord("d") or char == curses.KEY_RIGHT:
                right()
            elif char == ord("v"):
                print("[AI ?]: ")
                command = screen.getch()
                with picamera.PiCamera() as camera
                    camera.start_preview()
                    while True:
                        ret, frame = camera.read()
                        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
                        auxFrame = frame.copy()

                        color = (randint(0, 255), randint(0, 255), randint(0, 255))

                        faces = faceCascade.detectMultiScale(scaleFactor=1.1,
                                                             minNeighbors=5,
                                                             minSize=(30, 30))

                        upperBodies = upperBodyCascade.detectMultiScale(scaleFactor=1.1,
                                                              minNeighbors=5,
                                                              minSize=(30, 30))

                        lowerBodies = upperBodyCascade.detectMultiScale(scaleFactor=1.1,
                                                                        minNeighbors=5,
                                                                        minSize=(30, 30))

                        for (x, y, w, h) in faces:
                            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)

                        for (x, y, w, h) in upperBodies:
                            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)

                        for (x, y, w, h) in lowerBodies:
                            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)


                        if command == ord("y"):
                            cv2.imshow("Rusty - camera feed", frame)
                        elif command == ord("n"):
                            cv2.imshow("Rusty - camera feed", auxFrame)

                        if cv2.waitKey(2) and 0xFF == ord("x"):
                            camera.stop_preview()
                            break

            elif char == ord("c"):
                for i in range(len(motors)):
                    GPIO.output(motors[i], GPIO.LOW)


            elif char == ord("m"):
                print("[battery / solar]: ")
                command = screen.getch()
                if command == ord("b"):
                    os.system("python3 relays/solarSwitch.py --state no")
                    time.sleep(0.3)
                    os.system("python3 relays/motorsSwitch.py --state yes")
                elif command == ord("s"):
                    os.system("python3 relays/motorsSwitch.py --state no")
                    time.sleep(0.3)
                    os.system("python3 relays/solarSwitch.py --state yes")
                else:
                    os.system("python3 relays/motorsSwitch.py --state no")
                    time.sleep(0.3)
                    os.system("python3 relays/solarSwitch.py --state no")

            elif char == ord("q"):
                break

    except KeyboardInterrupt:
        GPIO.cleanup()

    finally:
        curses.nocbreak()
        screen.keypad(0)
        curses.echo()
        curses.endwin()

    GPIO.cleanup()