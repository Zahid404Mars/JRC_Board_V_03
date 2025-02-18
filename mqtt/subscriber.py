import time
import json
import paho.mqtt.client as mqtt
from random import randint
from datetime import datetime
def on_message(client, userdata, message):
    data = message.payload.decode("utf-8")
  
    # dict_data = json.loads(data)
    # SampleRate = dict_data["S"]
    print(f"The Sample Rate is => {data}")

broker = "mqtt.eclipseprojects.io"

client = mqtt.Client(client_id="scoplantuser", clean_session=True, userdata=None)

client.connect(broker)
client.loop_start()
while True:
    client.subscribe("scoplant/p/sensor/v1/7340941661")
    client.on_message = on_message
    time.sleep(5)