from websocket import create_connection

ws = create_connection("ws://192.168.0.102:80")
print("Sending 'Hello, World'...")
ws.send("taggleLed")
print("Sent")
print("Receiving...")
result = ws.recv()
print("Received '%s'" % result)
ws.close()