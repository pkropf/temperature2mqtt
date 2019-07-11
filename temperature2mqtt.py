#! /usr/bin/env python3.7

import paho.mqtt.client as mqtt
import Adafruit_DHT
import platform
import time
import configparser
import os
from configHelper import findConfig


keywords = os.environ.copy()
keywords['nodename'] = platform.node()

ini_file = findConfig('temperature2mqtt.ini')
config = configparser.ConfigParser()
config.read(ini_file)

broker = config.get('mqtt', 'host').format(**keywords)
broker_port = int(config.get('mqtt', 'port').format(**keywords))

dht_type = int(config.get('dht', 'type').format(**keywords))
dht_pin = int(config.get('dht', 'pin').format(**keywords))

# test if the broker has been configured, MQTT_BROKER is the default value in the
# config file as distributed from the repository
if broker == 'mqtt host':
    raise ValueError('broker not configured')

mqttc = mqtt.Client()
mqttc.connect(broker, broker_port)
mqttc.loop_start()

pause = int(config.get('general', 'pause').format(**keywords))
units = config.get('general', 'units').format(**keywords)
sensor_topic = config.get('topics', 'sensor').format(**keywords)

print(f"using configuration file {ini_file}")
print(f"using mqtt broker {broker} on via port {broker_port}")
print(f"using dht type {dht_type} on pin {dht_pin}")
print(f"publishing temperature to {sensor_topic} as {units}")

while True:
    humidity, temperature = Adafruit_DHT.read_retry(dht_type, dht_pin)
    status = 'Ok'

    if temperature == None:
        status = 'NoSensor'
        temperature = 0.0
        humidity = 0.0

    elif units in ['f', 'F']:
        temperature = (temperature * (9/5)) + 32

    sensor_data = f'{{"status": "{status}", "temperature": "{temperature:.1f}", "units": "{units}", "humidity": "{humidity:.1f}"}}'
    mqttc.publish(sensor_topic, sensor_data)

    print(sensor_data)

    time.sleep(pause)
