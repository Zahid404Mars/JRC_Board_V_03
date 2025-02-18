import time
import paho.mqtt.client as mqtt
from random import randint
import json
import datetime
mqttBroker = "mqtt.eclipseprojects.io"

client = mqtt.Client(client_id="scoplantadmin")
client.connect(mqttBroker)

str(datetime.date.today())
while True:
    our_data_in_dict = {
        "salinity": str(randint(1, 100)),
        "tds": str(randint(1, 100)),
        "humidity": str(randint(1, 100)),
        "temperature": str(randint(1, 100)),
        "nitrogen": str(randint(1, 100)),
        "phosporus": str(randint(1, 100)),
        "G": str(randint(1, 100)),
        "H": datetime.datetime.now().time().strftime("%H:%M:%S"),
        # "I": ,  we dont need date in jason here
        "J": str(randint(1, 100)),
        "K": str(randint(1, 100)),
        "L": str(randint(1, 100)),
    }
    
    data_json = json.dumps(our_data_in_dict)
    
    client.publish("scoplant/p/sensor/v1/14514413010", data_json)
    
    print("Message Send!")

    time.sleep(5)
