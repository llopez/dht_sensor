import network
import time

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)

def connect(config):
  if not sta_if.isconnected():
    print('WIFI: Connecting', end='')
    sta_if.connect(config['ssid'], config['pwd'])
    while not sta_if.isconnected():
      print('.', end='')
      time.sleep_ms(250)
  print('\nWIFI: network config:', sta_if.ifconfig())
  return sta_if.ifconfig()

def disconnect():
  if sta_if.isconnected():
    print('disconnecting from network', end='')
    sta_if.disconnect()
    while sta_if.isconnected():
      print('.', end='')
      time.sleep_ms(250)
  print('\nSuccessfully disconnected from network')
