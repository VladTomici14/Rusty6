import RPi.GPIO as GPIO
import time

#GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

motors = 25
solar = 8

try:
    while True:
        GPIO.setmode(GPIO.BCM)
        command = str(input(""))
        if command == "motorson":
            GPIO.cleanup()
            time.sleep(0.5)
            GPIO.setup(motors, GPIO.OUT)

        elif command == "motorsoff":
            GPIO.cleanup()

        elif command == "solaron":
            GPIO.cleanup()
            time.sleep(0.5)
            GPIO.setup(solar, GPIO.OUT)

        elif command == "solaroff":
            GPIO.cleanup()

        elif command == "exit":
            break
            
except KeyboardInterrupt:
    GPIO.cleanup()

time.sleep(2)
print("something")

GPIO.cleanup()