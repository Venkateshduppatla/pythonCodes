from tkinter import *
from tkinter import ttk
#from tkinter import messagebox
#from tkinter import scrolledtext
mainWindow = Tk()
mainWindow.title("Greet with Name")
mainWindow.geometry("300x400")

text = Entry(mainWindow, width = 50)
text.grid(column = 1, row = 3)

label = Label(mainWindow, text = "Login", bg = "green", fg = "red")

button1 = Button(mainWindow, text = "Welcome.", bg = "black", fg = "White")
button1.grid(column = 1, row = 1)

# radioButton1 = Radiobutton(mainWindow, text = "Radiobutton", bg = "Black", fg = "red", value = 1)
# radioButton1.grid(column = 1, row = 2)


# def messageButton():
# 	messagebox.showinfo("Status", "Hello")

# messageBox = Button(mainWindow, text = "Say Hello", command = messageButton, font = (20)).grid(column = 1, row = 4)

# n = StringVar()
# course = ttk.Combobox(mainWindow, textvariable = n)
# course["values"] = ("Python", "C", "C++", "Java", "Oracle", "Mysql", "DBMS")
# course.grid(column = 1, row = 5)
# course.current(1)
# print(n.get())

# text1 = scrolledtext.ScrolledText(mainWindow, wrap = WORD, width = 40,  height = 10)
# text1.grid(column = 1, row = 6)
# text1.focus()

mainWindow.mainloop()