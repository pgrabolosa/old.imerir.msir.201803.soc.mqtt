import paho.mqtt.client as mqtt
import json
from time import sleep
from random import random
import ssl

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))


client = mqtt.Client('d:15tzlo:typedemo:typedemo-3')
client.on_connect = on_connect
client.tls_set("bluemix.pem", tls_version=ssl.PROTOCOL_TLSv1_2)

client.username_pw_set("use-token-auth", "m27RKpMhTjVDF&KES6") #"cUs!)6grT7WT0P4ymZ")
client.connect("15tzlo.messaging.internetofthings.ibmcloud.com", 8883, 60)

temperature = 30.0

client.loop_start()
while True:
  sleep(2)
  temperature += random() - 0.5
  print "sending ", temperature
  payload = { 'temperature': temperature }
  client.publish("iot-2/evt/statusEvent/fmt/json", json.dumps({"d": payload}))
  