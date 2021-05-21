import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

motor_relay = 12
solar_relay = 23

GPIO.setup(motor_relay, GPIO.OUT)
GPIO.output(motor_relay, GPIO.LOW)

if __name__ == "__main__":
    command = str("enter: ")
    k = 0
    if command == k:
        k=k+1

    if k % 2 == False:
        GPIO.output(motor_relay, GPIO.LOW)
    else:
        GPIO.output(motor_relay, GPIO.HIGH)