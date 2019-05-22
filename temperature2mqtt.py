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

dht_type = config.getint('dht', 'type')
dht_port = config.getint('dht', 'port')

mqttc.connect(broker, broker_port)
mqttc.loop_start()

keywords = os.environ.copy()
keywords['nodename'] = platform.node()

pause = config.getint('general', 'pause')
units = config.get('general', 'units')
sensor_topic = config.get('topics', 'sensor').format(**keywords)

print(f"using configuration file {ini_file}")
print(f"using mqtt broker {broker} on via port {broker_port}")
print(f"using dht type {dht_type} on port {dht_port}")
print(f"publishing temperature to {sensor_topic} as {units}")

while True:
    humidity, temperature = Adafruit_DHT.read_retry(dht_type, dht_port)

    if units in ['f', 'F']:
        temperature = (temperature * (9/5)) + 32

    sensor_data = f'{{"temperature": "{temperature}", "units": "{units}", "humidity": "{humidity}"}}'
    mqttc.publish(sensor_topic, sensor_data)

    print(sensor_data)

    time.sleep(pause)
