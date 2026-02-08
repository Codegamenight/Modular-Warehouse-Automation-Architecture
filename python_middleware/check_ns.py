from opcua import Client

client = Client("opc.tcp://localhost:4840/freeopcua/server/")
client.connect()

print("Namespaces on server:")
for idx, ns in enumerate(client.get_namespace_array()):
    print(idx, ns)

client.disconnect()
