# Program to send mails using GUI.

import smtplib 
import sendgrid
from tkinter import *

class Gui: 
	def __init__(self):
		self.signinWindow = Tk()
		self.signinWindow.title("Sign in-Google Accounts")
		self.signinWindow.geometry("200x170")
		self.signinWindow.resizable(width = False, height = False)

		self.label_1 = Label(self.signinWindow, text = "Google", fg = "Black")
		self.label_1.grid(column = 3 , row = 2)
		self.label_2 = Label(self.signinWindow, text = "Sign in ", fg = "Black")
		self.label_2.grid(column = 3 , row = 3)
		self.label_3 = Label(self.signinWindow, text = "Use Your Google Account", fg = "Black")
		self.label_3.grid(column = 3 , row = 4)
		self.label_4 = Label(self.signinWindow, text = " Email ID", fg = "Black")
		self.label_4.grid(column = 3 , row = 5)
		self.entryUserName = Entry(self.signinWindow, width = 32)
		self.entryUserName.grid(column = 3, row = 6)
		self.entryUserName.focus()
		self.label_5 = Label(self.signinWindow, text = " Password", fg = "Black")
		self.label_5.grid(column = 3 , row = 7)
		self.entryPassword = Entry(self.signinWindow, width = 32)
		self.entryPassword.grid(column = 3, row = 8)
		self.entryPassword.config(show = "*")
		self.nextButton = Button(self.signinWindow, text = "sign in", bg = "blue", fg = "White", command = self.goAhed)
		self.nextButton.grid(column = 3, row = 9)

		self.signinWindow.mainloop()

	def goAhed(self):
		self.userName = self.entryUserName.get()
		self.password = self.entryPassword.get()
		self.signinWindow.destroy()
		self.composeWindow = Tk()
		self.composeWindow.title("New Message")
		self.composeWindow.geometry("500x550")
		self.composeWindow.resizable(width = False, height = False)

		self.fromLabel = Label(self.composeWindow, text = ("From: "), fg = "Black")
		self.fromLabel.place(relwidth = 0.2, relheight = 0.05, relx = 0.05, rely = 0.01)
		self.fromAddress = Label(self.composeWindow, text = self.userName, fg = "Black")
		self.fromAddress.place(relwidth = 0.75, relheight = 0.05, relx = 0.2, rely = 0.01)
		self.toLabel = Label(self.composeWindow, text = "To: ", fg = "Black")
		self.toLabel.place(relwidth = 0.2, relheight = 0.05, relx = 0.05, rely = 0.1)
		self.entryReceiverId = Entry(self.composeWindow, width = 60)
		self.entryReceiverId.place(relwidth = 0.75, relheight = 0.05, relx = 0.2, rely = 0.1)
		self.entryReceiverId.focus()
		self.ccLabel = Label(self.composeWindow, text = "CC: ", fg = "Black")
		self.ccLabel.place(relwidth = 0.2, relheight = 0.05, relx = 0.05, rely = 0.15)
		self.ccMail = Entry(self.composeWindow)
		self.ccMail.place(relwidth = 0.75, relheight = 0.05, relx = 0.2, rely = 0.15)
		self.subjectLabel = Label(self.composeWindow, text = "Subject: ", fg = "Black")
		self.subjectLabel.place(relwidth = 0.2, relheight = 0.05, relx = 0.05, rely = 0.25)
		self.subject = Entry(self.composeWindow)
		self.subject.place(relwidth = 0.75, relheight = 0.08, relx = 0.2, rely = 0.25)
		self.entryMessage = Text(self.composeWindow)
		self.entryMessage.place(relwidth = 1, relheight = 0.6, relx = 0, rely = 0.35)
		self.sendButton = Button(self.composeWindow, text = "Send", bg = "blue", fg = "White", command = self.sendMessage)
		self.sendButton.place(relwidth = 0.2, relheight = 0.05, relx = 0.8, rely = 0.95)

	def sendMessage(self):
		receiverMail = self.entryReceiverId.get()
		ccMail = [self.ccMail.get()]
		subjectMessage = self.subject.get()
		try: 
		    smtp = smtplib.SMTP('smtp.gmail.com', 587) 
		    smtp.starttls() 
		    smtp.login(self.userName, self.password)
		    message = self.entryMessage.get('1.0', END)
		    sendingMessage = "To: %s\n" %receiverMail + "CC: %s\n"%",".join(ccMail) + "Subject: %s\n" %subjectMessage + "\n" + message 
		    smtp.sendmail(self.userName, [receiverMail, ccMail], sendingMessage) 
		    smtp.quit() 
		    print ("Email sent successfully!") 

		except Exception as ex: 
		    print("Something went wrong....",ex)
g = Gui()		