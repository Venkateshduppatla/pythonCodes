import smtplib
from threading import Thread
from tkinter import *
from tkinter import font
from tkinter import ttk
class GUI:
    def __init__(self):
        self.Window = Tk()
        self.Window.withdraw()
        self.login = Tk()
        self.login.title("Login")
        self.login.configure(width = 500, height = 500)
        self.labelEmail = Label(self.login, text = "Email Id: ", font = "Helvetica 12")
        self.labelEmail.place(relheight = 0.2, relwidth = 0.2, relx = 0.1, rely = 0.2)
        self.entryEmail = Entry(self.login, font = "Helvetica 14")
        self.entryEmail.place(relwidth = 0.5, relheight = 0.2, relx = 0.3, rely = 0.2)
        self.labelPassword = Label(self.login, text = "Password: ", font = "Helvetica 12")
        self.labelPassword.place(relheight = 0.2, relwidth = 0.2, relx = 0.1, rely = 0.4)
        self.entryPassword = Entry(self.login, font = "Helvetica 14")
        self.entryPassword.place(relwidth = 0.5, relheight = 0.2, relx = 0.3, rely = 0.4)
        self.entryPassword.config(show = "*")
        self.entryEmail.focus()
        self.login.bind('<Return>', self.enter)
        self.Window.mainloop()
    def enter(self, e):
        self.compose()
    def compose(self):
        self.senderMail = self.entryEmail.get()
        self.senderPassword = self.entryPassword.get()
        self.login.destroy()
        self.Window.deiconify()
        self.Window.title("COMPOSE")
        self.Window.configure(width = 500, height = 500, bg = "#17202A")
        self.fromMail = Label(self.Window, text = "From: " + self.senderMail, font = "Helvetica 13 bold", bg = "#17202A", fg = "#EAECEE")
        self.fromMail.place(relheight = 0.09, rely = 0, relwidth = 1, relx = 0.05)
        self.toMail = Label(self.Window, text = "To", font = "Helvetica 13 bold", bg = "#17202A", fg = "#EAECEE")
        self.toMail.place(relheight = 0.09, rely = 0.1, relwidth = 0.15, relx = 0.05)
        self.entryToMail = Entry(self.Window, font = "Helvetica 14")
        self.entryToMail.place(relheight = 0.09, rely = 0.1, relwidth = 0.7, relx = 0.3)
        self.subject = Label(self.Window, text = "Subject", font = "Helvetica 13 bold", bg = "#17202A", fg = "#EAECEE")
        self.subject.place(relheight = 0.09, rely = 0.2, relwidth = 0.15, relx = 0.05)
        self.entrySubject = Entry(self.Window, font = "Helvetica 14")
        self.entrySubject.place(relheight = 0.09, rely = 0.2, relwidth = 0.7, relx = 0.3)
        self.CC = Label(self.Window, text = "CC", font = "Helvetica 13 bold", bg = "#17202A", fg = "#EAECEE")
        self.CC.place(relheight = 0.09, rely = 0.3, relwidth = 0.15, relx = 0.05)
        self.entryCC = Entry(self.Window, font = "Helvetica 14")
        self.entryCC.place(relheight = 0.09, rely = 0.3, relwidth = 0.7, relx = 0.3)
        self.textArea = Text(self.Window, font = "Helvetica 14")
        self.textArea.place(relheight = 0.4, rely = 0.4, relwidth = 1)
        self.entryToMail.focus()
        self.send = Button(self.Window, text = "Send", font = "Helvetica 10 bold", command = lambda : self.sendButton(self.textArea.get("1.0", END)))
        self.send.place(relheight = 0.1, rely = 0.8, relx = 0, relwidth = 1)
        message = "From: %s\r\n"%(self.senderMail) + "To: %s\r\n"%(self.entryToMail.get()) + "CC: %s\r\n"%",".join([self.entryCC.get()]) + "Subject: %s\r\n\n"%self.entrySubject.get() +"\r\n" + self.textArea.get('1.0', END)
        self.receiverMail = [self.entryToMail.get(), self.entryCC.get()]
    def sendButton(self, message):
        try: 
            smtp = smtplib.SMTP('smtp.gmail.com', 587) 
            smtp.starttls() 
            smtp.login(self.senderMail, self.senderPassword)
            smtp.sendmail(self.senderMail, self.receiverMail, message) 
            smtp.quit() 
            print ("Email sent successfully!") 
        except Exception as ex: 
            print("Something went wrong....",ex)
g = GUI()