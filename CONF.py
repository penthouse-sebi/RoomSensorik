

NETWORK_PROFILES = 'wifi.dat'
CONF_FILE = 'conf.dat'
SENSOR_FILE = 'sensor.dat'

DEFAULT_HOST_IP = '10.0.0.4'
DEFAULT_MQTT_SUB_TOPIC = 'RoomSensorik'
DEFAULT_MQTT_PUB_TOPIC = 'HA'

HOTSPOT_SSID = "RoomSensorik"
HOTSPOT_PASSWORD = "RoomSensorik"
AUTHMODE = 3  # WPA2
NETWORK_PROFILES = 'wifi.dat'
RESET_DEL_FILES = ['wifi.dat']


RESET_DELAY = 0.5
RESET_LED = 16
RESET_BTN = 14

PIN_SCL = 22
PIN_SDA = 21

SENSORS_SLEEP = 10


MAIN_URL = "https://raw.githubusercontent.com/penthouse-sebi/EspSensorik/master/"
# UPGRADE_FILES = ["BME280.py", "boot.py", "CCS811.py", "CONF.py", "main.py", "mqtt.py", "umqttsimple.py", "wifimgr.py"]

UPGRADE_FILES = ["main.py"]