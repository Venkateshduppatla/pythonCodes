# Server program to forward messages from client to client.

from threading import Thread
from socket import *
addressList = []
chatHistory = []
def forwardReceviedMessages(client, name):
	while True:
		message = client.recv(1024).decode()
		chatHistory.append(message)
		sendAll(message)
def sendAll(message):
	for address in addressList:
		address.send(str.encode(message))
# serverIpAdress = '192.168.0.103'
serverIpAdress = 'localhost'
serverPort = 9999
serverSocket = socket(AF_INET,SOCK_STREAM)
print("waiting....")
serverSocket.bind((serverIpAdress, serverPort))
serverSocket.listen()
while True:
	clientSocket, clientAddress = serverSocket.accept()
	name = clientSocket.recv(1024).decode()
	sendAll(name + " joined\n")
	addressList.append(clientSocket)
	for chat in chatHistory:
		clientSocket.send(str.encode(chat + "\n\n"))
	print("Connented with: ", clientAddress)
	# print(chatHistory)
	Thread(target = forwardReceviedMessages, args = (clientSocket, name)).start()
