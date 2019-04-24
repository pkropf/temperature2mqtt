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
broker = config.get('mqtt', 'host')
broker_port = config.getint('mqtt', 'port')
mqttc.connect(broker, broker_port)
mqttc.loop_start()

keywords = os.environ.copy()
keywords['nodename'] = platform.node()

pause = config.getint('general', 'pause')
temperature_topic = config.get('topics', 'temperature').format(**keywords)
humidity_topic = config.get('topics', 'humidity').format(**keywords)

print(f"using mqtt broker {broker} on via port {broker_port}")
print(f"publishing temperature to {temperature_topic}")
print(f"publishing humidity to {humidity_topic}")

while True:
    humidity, temperature = Adafruit_DHT.read_retry(11, 4)

    mqttc.publish(temperature_topic, temperature)
    mqttc.publish(humidity_topic,    humidity)

    ftemperature = (temperature * (9/5)) + 32
    print(f'Temp: {temperature} C, {ftemperature} f  Humidity: {humidity}')

    time.sleep(pause)
