import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

relay = 12
GPIO.setup(relay, GPIO.OUT)
GPIO.output(relay, GPIO.LOW)
GPIO.output(relay, GPIO.HIGH)

GPIO.setwarnings(False)