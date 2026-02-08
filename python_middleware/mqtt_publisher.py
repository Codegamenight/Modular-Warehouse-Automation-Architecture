import paho.mqtt.client as mqtt
import json
import random
import time

broker = "broker.hivemq.com"
port = 1883
topic = "warehouse/telemetry"

client = mqtt.Client("AutomationMiddleware")
client.connect(broker, port)

while True:
    payload = {
        "conveyor_speed": random.randint(0,100),
        "robot_status": random.choice(["Idle","Busy","Fault"]),
        "fault_signal": random.choice([0,1])
    }
    client.publish(topic, json.dumps(payload))
    print(f"Published: {payload}")
    time.sleep(5)
