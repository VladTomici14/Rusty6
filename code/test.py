import RPi.GPIO as GPIO
import time

#GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

motors = 25
solar = 8
GPIO.setup(motors, GPIO.OUT)
GPIO.setup(solar, GPIO.OUT)

for i in range(3):
    GPIO.output(motors, GPIO.HIGH)
    print("bababoi")
    time.sleep(1)
    GPIO.output(motors, GPIO.LOW)
    print("babanoi")

"""
try:
    while True:
        command = str(input(""))
        if command == "motorson":
            
        elif command == "motorsoff":
            
        elif command == "solaron":
            
        elif command == "solaroff";
        
        elif command == "exit":
            break
            
except KeyboardInterrupt:
    GPIO.cleanup()
"""

time.sleep(2)
print("something")

GPIO.cleanup()