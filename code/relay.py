import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

motor_relay = 12
solar_relay = 23

GPIO.setup(motor_relay, GPIO.OUT)
GPIO.output(motor_relay, GPIO.LOW)

time.sleep(2)

GPIO.output(motor_relay, GPIO.HIGH)
time.sleep(4)
GPIO.output(motor_relay, GPIO.LOW)

"""if __name__ == "__main__":
    while True:
        command = str(input("enter: "))
        k = 0
        if command == "k":
            k = k + 1
        elif command == "q":
            break

        if k % 2 == False:
            GPIO.output(motor_relay, GPIO.LOW)
        elif k % 2 == True:
            GPIO.output(motor_relay, GPIO.HIGH)"""