from opcua import Client
import time
import random

SERVER_URL = "opc.tcp://localhost:4840/freeopcua/server/"
NAMESPACE = 2  # Correct namespace for your variables

# Connect to OPC UA server with retry
client = Client(SERVER_URL)

for attempt in range(5):
    try:
        client.connect()
        print("Connected to OPC UA Server")
        break
    except Exception as e:
        print(f"Connection failed, retrying... ({attempt+1}/5)")
        time.sleep(2)
else:
    print("Could not connect to OPC UA Server. Exiting.")
    exit(1)

# Access nodes
conveyor_speed_node = client.get_node(f"ns={NAMESPACE};s=ConveyorSpeed")
robot_status_node    = client.get_node(f"ns={NAMESPACE};s=RobotStatus")
fault_signal_node    = client.get_node(f"ns={NAMESPACE};s=FaultSignal")

try:
    while True:
        conveyor_speed = random.randint(0, 100)
        robot_status    = random.randint(0, 2)
        fault_signal    = random.randint(0, 1)

        try:
            conveyor_speed_node.set_value(conveyor_speed)
            robot_status_node.set_value(robot_status)
            fault_signal_node.set_value(fault_signal)
            print(f"Conveyor: {conveyor_speed}, Robot: {robot_status}, Fault: {fault_signal}")
        except Exception as e:
            print("Write error:", e)

        time.sleep(2)

finally:
    client.disconnect()
    print("Disconnected from OPC UA Server")

