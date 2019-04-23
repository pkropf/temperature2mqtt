#! /usr/bin/env python3.7

import paho.mqtt.client as mqtt
import Adafruit_DHT
import platform
import time
import configparser
import os


config = configparser.ConfigParser()
ini_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'temperature2mqtt.ini')
config.read(ini_file)

mqttc = mqtt.Client()
mqttc.connect(config.get('mqtt', 'host'), config.getint('mqtt', 'port') )
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
