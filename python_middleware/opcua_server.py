from opcua import Server
import time

# Create the server instance
server = Server()

# Set endpoint accessible from LAN
# Replace 192.168.0.24 with your machine's IPv4 address if different
server.set_endpoint("opc.tcp://192.168.0.24:4840/freeopcua/server/")

# Setup a custom namespace
uri = "http://modular-warehouse-automation"
idx = server.register_namespace(uri)

# Create a "Warehouse" object under Objects node
warehouse = server.nodes.objects.add_object(idx, "Warehouse")

# Add variables to the warehouse object
conveyor_speed = warehouse.add_variable(idx, "ConveyorSpeed", 0.0)  # float
conveyor_speed.set_writable()

robot_status = warehouse.add_variable(idx, "RobotStatus", 0)  # int
robot_status.set_writable()

fault_signal = warehouse.add_variable(idx, "FaultSignal", False)  # bool
fault_signal.set_writable()

# Start the server
server.start()
print("OPC UA Server started at opc.tcp://192.168.0.24:4840/freeopcua/server/")

try:
    # Keep the server running
    while True:
        time.sleep(1)

finally:
    server.stop()
    print("OPC UA Server stopped")

    

    
