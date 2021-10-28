import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('127.0.0.1', 4444))

client.send(b'Hello world')
print(client.recv(2048))

client.close()
