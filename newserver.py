# # # Server code for two clients. 

import socket
from threading import Thread

def receiveMessages(client):
	while 1:
		clientMessage = client.recv(1024).decode()
		chatHistory.append(clientMessage)
		sendMessages(clientMessage)
def sendMessages(clientMessage):
	for address in clientsAddressList:
		address.send(str.encode(clientMessage))
serverIpAddress = "localhost"
port = 25955
server = socket.socket()
print("Waiting for Connection...")
server.bind((serverIpAddress, port))
server.listen(1)
clientsAddressList = []
chatHistory = []
while 1:
	client, clientIPAddress = server.accept()
	print(clientIPAddress)
	print("Connected with", clientIPAddress)
	name = client.recv(1024).decode()
	sendMessages(name + " Joined!")
	clientsAddressList.append(client)
	for message in chatHistory:
		client.send(str.encode(message + "\n"))
	Thread(target = receiveMessages, args = (client, )).start()


# # Server code for two clients. 

# import socket
# import jpysocket
# from threading import Thread

# # def receiveMessages(client):
# # 	while 1:
# # 		clientMessage = client.recv(1024).decode()
# # 		chatHistory.append(clientMessage)
# # 		sendMessages(clientMessage)
# # def sendMessages(clientMessage):
# # 	for address in clientsAddressList:
# # 		address.send(str.encode(clientMessage))
# serverIpAddress = "localhost"
# port = 25955
# server = socket.socket()
# print("Waiting for Connection...")
# server.bind((serverIpAddress, port))
# server.listen(1)
# while 1:
# 	client, clientIPAddress = server.accept()
# 	sendMessage = jpysocket.jpyencode("")
# 	client.send(sendMessage)
# 	fromClient = client.recv(1024)
# 	fromClient = jpysocket.jpydecode(fromClient)
# 	print("Message From Client: " + fromClient)
# 	toClient = jpysocket.jpyencode(input("Enter the message: "))
# 	client.send(toClient)

# import socket
# from threading import Thread

# ipAddress = 'localhost'
# portNumber = 2590
# client = socket.socket()
# client.bind((ipAddress, portNumber))
# client.listen(1)
# # name = input('Enter Your Name: ')
# # client.send(str.encode(name))
# # print(client.recv(1024).decode())
# def receiveMessage():
# 	while True:
# 		print(client.recv(1024).decode())

# def sendMessage():
# 	while True:
# 		client.send(str.encode("Message From " + name + ": " + input("")))

# Thread(target = receiveMessage).start()
# Thread(target = sendMessage).start()