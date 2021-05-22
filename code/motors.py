import RPi.GPIO as GPIO
import time
import curses
import cv2
from picamera import PiCamera
from tkinter import *

root = Tk()
root.title("Rusty control pannel")
root.geometry("1080x720")
root.mainloop()

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

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

def forward():
    GPIO.output(forward1, GPIO.HIGH)
    GPIO.output(backward1, GPIO.LOW)

    GPIO.output(forward2, GPIO.HIGH)
    GPIO.output(backward2, GPIO.LOW)

    GPIO.output(forward3, GPIO.HIGH)
    GPIO.output(backward3, GPIO.LOW)

    GPIO.output(forward4, GPIO.HIGH)
    GPIO.output(backward4, GPIO.LOW)

def backward():
    GPIO.output(forward1, GPIO.LOW)
    GPIO.output(backward1, GPIO.HIGH)

    GPIO.output(forward2, GPIO.LOW)
    GPIO.output(backward2, GPIO.HIGH)

    GPIO.output(forward3, GPIO.LOW)
    GPIO.output(backward3, GPIO.HIGH)

    GPIO.output(forward4, GPIO.LOW)
    GPIO.output(backward4, GPIO.HIGH)

def right():
    GPIO.output(forward1, GPIO.HIGH)
    GPIO.output(backward1, GPIO.LOW)

    GPIO.output(forward2, GPIO.LOW)
    GPIO.output(backward2, GPIO.HIGH)

    GPIO.output(forward3, GPIO.HIGH)
    GPIO.output(backward3, GPIO.LOW)

    GPIO.output(forward4, GPIO.LOW)
    GPIO.output(backward4, GPIO.HIGH)

def left():
    GPIO.output(forward1, GPIO.LOW)
    GPIO.output(backward1, GPIO.HIGH)

    GPIO.output(forward2, GPIO.HIGH)
    GPIO.output(backward2, GPIO.LOW)

    GPIO.output(forward3, GPIO.LOW)
    GPIO.output(backward3, GPIO.HIGH)

    GPIO.output(forward4, GPIO.HIGH)
    GPIO.output(backward4, GPIO.LOW)

camera = PiCamera()

if __name__ == "__main__":
    try:
        while True:
            char = screen.getch()
            if char == ord("w") or char == curses.KEY_UP:
                forward()
                print("f")
            elif char == ord("a") or char == curses.KEY_LEFT:
                left()
                print("l")
            elif char == ord("s") or char == curses.KEY_DOWN:
                backward()
                print("b")
            elif char == ord("d") or char == curses.KEY_RIGHT:
                right()
                print("r")
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