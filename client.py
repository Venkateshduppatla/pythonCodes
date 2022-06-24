# Client


# import socket

# client = socket.socket()
# client.connect('192.168.1.3', 4500)

# print(client.recv(1024).decode())


import socket

client = socket.socket()
client.connect(('192.168.1.3', 4500))
textMessage = input('Enter Your Message: ')
client.send(str.encode(textMessage))
print("Message from server: ", client.recv(1024))
client.close()