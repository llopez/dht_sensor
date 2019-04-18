import wifi
import mqtt
import config
import machine
from machine import Pin
import time
import dht

CONFIG = config.get()
TEMP_TOPIC = CONFIG['temp_topic']
HUM_TOPIC = CONFIG['hum_topic']

wifi.connect(CONFIG)
mqtt_client = mqtt.start(CONFIG)
mqtt_client = mqtt.connect(mqtt_client)
d = dht.DHT22(Pin(4))

while True:
  try:
    d.measure()
    temp = d.temperature()
    hum = d.humidity()
    mqtt_client.publish(str.encode(TEMP_TOPIC), str.encode(str(temp)))
    mqtt_client.publish(str.encode(HUM_TOPIC), str.encode(str(hum)))
  except OSError as e:
    machine.reset()
  time.sleep(5)
