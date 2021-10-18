from websocket import create_connection

ws = create_connection("ws://192.168.43.41:80")
print("Sending 'Hello, World'...")
ws.send("syske master\n ha ha ha ha......hello world!!!")
print("Sent")
print("Receiving...")
result = ws.recv()
print("Received '%s'" % result)
ws.close()