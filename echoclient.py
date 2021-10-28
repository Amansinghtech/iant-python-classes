import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('127.0.0.1', 4444))

while True:
    data = input("Message: ")
    client.send(data.encode())
    print("Echo reply: ", client.recv(2048).decode())
    if data == "exit":
        client.close()
        break
