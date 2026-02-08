from opcua import Client
import time
import random

# OPC UA Server (simulated PLC)
url = "opc.tcp://localhost:4840/freeopcua/server/"
client = Client(url)

try:
    client.connect()
    print("Connected to OPC UA Server")

    while True:
        # Simulate sensor values
        conveyor_speed = random.randint(0, 100)
        robot_status = random.choice([0,1,2])  # 0=Idle,1=Busy,2=Fault
        fault_signal = random.choice([0,1])

        # Write values to OPC UA nodes
        client.get_node("ns=2;s=ConveyorSpeed").set_value(conveyor_speed)
        client.get_node("ns=2;s=RobotStatus").set_value(robot_status)
        client.get_node("ns=2;s=FaultSignal").set_value(fault_signal)

        print(f"Conveyor: {conveyor_speed}, Robot: {robot_status}, Fault: {fault_signal}")
        time.sleep(2)

finally:
    client.disconnect()
