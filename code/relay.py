import RPi.GPIO as GPIO
import time

# GPIO.setwarnings(False)

def relayOn(relay):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(relay, GPIO.OUT)

def relayOff():
    GPIO.cleanup()

GPIO.setmode(GPIO.BCM)
motors = 25
solar = 8

if __name__ == "__main__":
    try:
        while True:
            command = str(input(""))
            if command == "motors on":
                relayOff()
                relayOn(motors)

            elif command == "motors off":
                relayOff()

            elif command == "solar on":
                relayOff()
                relayOn(solar)

            elif command == "solar off":
                relayOff()

    except KeyboardInterrupt:
        GPIO.cleanup()
    finally:
        GPIO.cleanup()