from umqtt.simple import MQTTClient
import time

def start(config):
  client = MQTTClient(config['mqtt_client_id'], config['mqtt_ip'])
  return client

def is_connected(client):
  try:
    client.ping()
    return True
  except:
    return False

def connect(client):
  if is_connected(client):
    print('MQTT: Already connected')
  else:
    print('MQTT: Connecting', end='')
    try:
      client.connect()
      print('MQTT: Connected')
    except OSError as e:
      print('.', end='')
      time.sleep_ms(250)
      connect(client)
  return client
