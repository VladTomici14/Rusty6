import RPi.GPIO as GPIO
import time

#GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

motors = 25
solar = 8

try:
    while True:
        command = str(input(""))
        if command == "motorson":
            GPIO.output(solar, GPIO.LOW)
            time.sleep(0.3)
            GPIO.output(motors, GPIO.HIGH)

        elif command == "motorsoff":
            GPIO.output(motors, GPIO.LOW)

        elif command == "solaron":
            GPIO.output(motors, GPIO.LOW)
            time.sleep(3)
            GPIO.output(solar, GPIO.HIGH)

        elif command == "solaroff":
            GPIO.output(solar, GPIO.LOW)

        elif command == "exit":
            break
            
except KeyboardInterrupt:
    GPIO.cleanup()

time.sleep(2)
print("something")

GPIO.cleanup()