# Basic Program on binding enter key.
import socket
from tkinter import *
#from tkinter import ttk
#serverIp = "localhost"
#port= 25955
# client = socket.socket()
# client.connect(serverIp, port)
class ChatGui:
    def __init__(self):
        self.loginWindow = Tk()
        self.loginWindow.title("Login")
        self.loginWindow.geometry("300x400")

        self.loginTextLabel = Label(self.loginWindow, text = "Please Login to Continue", justify = CENTER, bg = white, fg = black, font = ("Times", 18))
        self.loginTextLabel.place(relheight = 0.15, relx = 0.2, rely = 0.07)
        self.loginWindow.mainloop()



# label = Label(mainWindow, text = "Name: ", bg = "white", fg = "Black")
# label.grid(column = 1 , row = 2)

# name = Entry(mainWindow, width = 20)
# name.grid(column = 2, row = 2)
# name.focus()


# def printName(e):
#     label = Label(mainWindow, text = ("Hi " + name.get() + "!"), bg = "white", fg = "Black")
#     label.grid(column = 2 , row = 5)

# mainWindow.bind('<Return>', printName)
