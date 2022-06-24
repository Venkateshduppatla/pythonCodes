import socket
from tkinter import *
from tkinter import font
from tkinter import ttk

mainWindow = Tk()
mainWindow.title("Chat Box")
mainWindow.geometry("300x400")


label = Label(mainWindow, text = "Login to COntinue: ", bg = "white", fg = "Black")
label.grid(column = 1 , row = 2)

name = Entry(mainWindow, width = 20)
name.grid(column = 2, row = 2)
name.focus()


# def printName(e):
#     label = Label(mainWindow, text = ("Hi " + name.get() + "!"), bg = "white", fg = "Black")
#     label.grid(column = 2 , row = 5)

# mainWindow.bind('<Return>', printName)

mainWindow.mainloop()


