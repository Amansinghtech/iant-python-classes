import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 4444))
server.listen(5)

client_sock, addr = server.accept()

print(addr)

data = client_sock.recv(2048)
print(data.decode())
client_sock.send(data)

server.close()
