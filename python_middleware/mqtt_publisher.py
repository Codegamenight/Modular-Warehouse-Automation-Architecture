import paho.mqtt.client as mqtt
import json
import random
import time

broker = "broker.hivemq.com"
port = 1883
topic = "warehouse/telemetry"

try:
    client = mqtt.Client("AutomationMiddleware")
    client.connect(broker, port)
except Exception as e:
    print(f"Failed to connect to MQTT broker: {e}")
    exit(1)


try:
    while True:
        payload = {
            "conveyor_speed": random.randint(0,100),
            "robot_status": random.choice(["Idle","Busy","Fault"]),
            "fault_signal": random.choice([True, False])
        }
        client.publish(topic, json.dumps(payload))
        print(f"Published: {payload}")
        time.sleep(5)
except KeyboardInterrupt:
    print("Stopping publisher...")
    client.disconnect()

