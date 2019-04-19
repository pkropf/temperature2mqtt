#! /usr/bin/env python3.7

import paho.mqtt.client as mqtt
import Adafruit_DHT
import platform
import time

mqttc = mqtt.Client()
mqttc.connect("localhost")
mqttc.loop_start()
nodename = platform.node()
pause = 30


while True:
    humidity, temperature = Adafruit_DHT.read_retry(11, 4)

    mqttc.publish(f"sensor/{nodename}/0/temperature", temperature)
    mqttc.publish(f"sensor/{nodename}/0/humidity",    humidity)

    ftemperature = (temperature * (9/5)) + 32
    print(f'Temp: {temperature} C, {ftemperature} f  Humidity: {humidity}')

    time.sleep(pause)
