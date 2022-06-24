# Server program.

import socket
server = socket.socket()
print("Socket Created")
server.bind(('192.168.1.3', 4500))
server.listen(3)
print("Waiting for connections")

while 1:
	client, address = server.accept()
	print("Connected with ", address)
	print(client)
	print(client.recv(1024).decode())
	client.send(str.encode(input("Enter message: ")))
	client.close()