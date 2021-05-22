import time
from pi_sht1x import SHT1x as sht
import RPi.GPIO as GPIO

dat = 2
sck = 3

with sht(dat, sck, gpio_mode = GPIO.BCM) as sensor:
    temperature = sensor.read_temperature()
    humidity = sensor.read_humidity(temperature)
    print(sensor)


