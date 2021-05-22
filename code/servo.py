import RPi.GPIO as GPIO
import time
import curses

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True

GPIO.setmode(GPIO.BCM)

servo1 = 4
servo2 = 5

GPIO.setup(servo1, GPIO.OUT)
pwm = GPIO.PWM(servo1, 50)

pwm.start(0)

def setAngle(angle):
    duty = angle / 18 + 2
    GPIO.output(servo1, GPIO.HIGH)
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)
    GPIO.output(servo1, GPIO.LOW)
    pwm.ChangeDutyCycle(0)

startAngle = str(input("start angle: "))

try:
    while True:
        char = screen.getch()

        if char == curses.KEY_UP:
            k = k + 5
        elif char == curses.KEY_DOWN:
            k = k - 5
setAngle(30)
pwm.stop()
GPIO.cleanup()