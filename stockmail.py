# Program to send a mail of order Items

import smtplib
import ssl
import mysql.connector as mysql
# import pandas as pd
import time as Time

HOST = "165.22.14.77"
DATABASE = "dbVenkatesh"
USER = "venkatesh"
PASSWORD = "pwdvenkatesh"
while(1):
	connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD)
	cursor = connection.cursor()
	port = 587  
	smtp_server = "smtp.gmail.com"
	sender = "venkivenkatesh2699@gmail.com"
	sender_password = "venki@C5"
	cursor.execute('SELECT supplier.supplierEMail, item.orderQuantity, orderItems.itemId, item.description FROM supplier, orderItems, item WHERE orderItems.itemId = item.itemId AND supplier.supplierId = item.supplierId')
	composeMail = cursor.fetchall()
	if (composeMail != []):
		recipient = composeMail[0][0]
		# ccMailId = 'ravi_pendyala@tecnics.com'
		ccMailId = 'harsha220217@gmail.com'
		message = ("CC: " + ccMailId + "\nSubject: Placing Order from DMart Yelamanchili!\n\nThe item " + composeMail[0][3] + " with ID " + composeMail[0][2] + " of " + str(composeMail[0][1]) + " Quantity is needed to DMart Yelamanchili.\nSend the Order as early as possible.\n\n\n\nRegards\nStore Manager,\nDMart Yelamanchili." )
		# print("CC: " + ccMailId + "\nSubject: Placing Order from DMart Yelamanchili!\n\nThe item " + composeMail[0][3] + " with ID " + composeMail[0][2] + " of " + str(composeMail[0][1]) + " Quantity is needed to DMart Yelamanchili.\nSend the Order as early as possible.\n\n\n\nRegards\nStore Manager,\nDMart Yelamanchili." )
		SSL_context = ssl.create_default_context()
		with smtplib.SMTP(smtp_server, port) as server:
			server.starttls(context=SSL_context)
			server.login(sender, sender_password)
			server.sendmail(sender, [recipient, ccMailId], message)
		print("Email Sent Succesfully!")
		cursor.execute('DELETE FROM orderItems')
		connection.commit()
	Time.sleep(20)
	connection.close()