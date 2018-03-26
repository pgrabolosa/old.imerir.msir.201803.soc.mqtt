import paho.mqtt.client as mqtt
from time import sleep
from random import random

client = mqtt.Client()
client.connect("127.0.0.1", 1883, 60)

temperature = 30.0

client.loop_start()
while True:
  sleep(2)
  temperature += random() - 0.5
  client.publish("maison1/temperature", temperature)