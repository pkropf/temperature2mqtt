#! /usr/bin/env python3.7

import sys
import Adafruit_DHT

while True:
    humidity, temperature = Adafruit_DHT.read_retry(11, 4)
    ftemperature = (temperature * (9/5)) + 32
    print(f'Temp: {temperature} C, {ftemperature} f  Humidity: {humidity}')
