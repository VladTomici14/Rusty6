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
                time.sleep(1)
                relayOn(motors)

            elif command == "motors off":
                relayOff()
                time.sleep(1)

            elif command == "solar on":
                relayOff()
                time.sleep(1)
                relayOn(solar)

            elif command == "solar off":
                time.sleep(1)
                relayOff()

    except KeyboardInterrupt:
        GPIO.cleanup()
    finally:
        GPIO.cleanup()