import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('127.0.0.1', 4444))
server.listen(5)
print("Listening on {}:{}".format('127.0.0.1', 4444))

c, addr = server.accept()
print("Got connection on {}:{}".format(addr[0], addr[1]))
while True:
    data = c.recv(2048)
    if data:
        print(data.decode())
        c.send(data)
    else:
        c.close()
        break
server.close()
