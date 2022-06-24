# Client

import socket
from threading import Thread
from tkinter import *
from tkinter import scrolledtext

ipAddress = '165.22.14.77'
portNumber = 9979
client = socket.socket()
client.connect((ipAddress, portNumber))

class Gui:
	def __init__(self):
		self.chatWindow = Tk()
		self.chatWindow.withdraw()
		self.loginWindow = Tk()
		self.loginWindow.geometry("300x150")
		self.loginWindow.title("Login Page.")
		self.note = Label(self.loginWindow, text = "Please Login To Continue.")
		self.note.place(relwidth = 0.8, relheight = 0.1, relx = 0.1, rely = 0.1)

		self.nameLable = Label(self.loginWindow, text = "Name: ")
		self.nameLable.place(relwidth = 0.2, relheight = 0.1, relx = 0.1, rely = 0.3)

		self.nameTextBox = Entry(self.loginWindow, width = 20)
		self.nameTextBox.place(relwidth = 0.6, relheight = 0.1, relx = 0.3, rely = 0.3)

		self.continueButton = Button(self.loginWindow, text = "continue", command = lambda: self.chatWindows(self.nameTextBox.get()))
		self.continueButton.place(relwidth = 0.4, relheight = 0.1, relx = 0.3, rely = 0.5)

		self.chatWindow.mainloop()

	def chatWindows(self, name):
		self.loginWindow.destroy()
		self.chatWindow.deiconify()
		client.send(str.encode(name))
		self.chatWindow.title(name)
		self.chatWindow.geometry("300x400")
		self.chatArea = scrolledtext.ScrolledText(self.chatWindow)
		self.chatArea.place(relx = 0, rely = 0, relheight = 0.9, relwidth = 1)
		self.chatArea.config(cursor = "arrow")
		self.chatArea.config(state = DISABLED)
		self.message = Entry(self.chatWindow, width = 40, bg = "lightgray")
		self.message.place(relx = 0, rely = 0.9, relheight = 0.1, relwidth = 0.8)
		Thread(target = self.receiveMessage).start()
		self.button = Button(self.chatWindow, text = ">>", command = lambda: self.sendMessage(name), width = 6)
		self.button.place(relx = 0.8, rely = 0.90, relheight = 0.1, relwidth = 0.2)

	def sendMessage(self, name):
		client.send(str.encode(name + ": " + self.message.get()))
		self.message.delete(0, END)


	def receiveMessage(self):
		while True:
			messages = client.recv(1024).decode()
			self.chatArea.config(state = NORMAL)
			self.chatArea.insert('end', messages + "\n")
			self.chatArea.config(state = DISABLED)

g = Gui()
