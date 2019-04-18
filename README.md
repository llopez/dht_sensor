# DHT Sensor
Embedded micropython code for an esp8266 that takes measurements and publishes them to a mqtt topic

## Features:
* It connects to a wifi network
* It connects to a mqtt broker
* It publishes temperature and humidity measurements to an mqtt topic

## Setup
Create config.json from config.json.example, replace with your configuration

```
cp config.json.example config.json
```

Copy files to the microcontroller

```
ampy --port /dev/tty.SLAB_USBtoUART --baud 115200 put config.json
ampy --port /dev/tty.SLAB_USBtoUART --baud 115200 put config.py
ampy --port /dev/tty.SLAB_USBtoUART --baud 115200 put main.py
ampy --port /dev/tty.SLAB_USBtoUART --baud 115200 put mqtt.py
ampy --port /dev/tty.SLAB_USBtoUART --baud 115200 put wifi.py
```

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/llopez/dht_sensor

## License

The code is available as open source under the terms of the [MIT License](https://opensource.org/licenses/MIT).

