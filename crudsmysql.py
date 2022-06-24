# Cruds Operation Program using Sqlite

import mysql.connector
import pandas as pd
import otp

class BankCustomers:
	def __init__(self):
		self.connection = mysql.connector.connect(host = '165.22.14.77', user = 'venkatesh', password = 'pwdvenkatesh', database = 'dbVenkatesh')
		self.cursor = self.connection.cursor()
		

	def createRecord(self):
		accountNumber = input("Enter the Account Number: ")
		name = input("Enter the Customer Name: ")
		balance = input("Enter the Balance: ")
		status = 'O'
		self.cursor.execute("INSERT INTO bankcustomers VALUES" + str((accountNumber, name, balance, status)))
		print("\nAccount Opened!")
		self.connection.commit()

	def  displayRecords(self):
		self.cursor.execute("SELECT * FROM bankcustomers")
		bankCustomerRecords = self.cursor.fetchall()
		for record in bankCustomerRecords:
			print("Account Number: ", record[0])
			print("Customer Name: ", record[1])
			print("Balance: ", record[2])
			if record[3] == 'O':
				print("Status: Account is Active!")
			else:
				print("Status: Account Closed!")

	# def displayRecords(self):
	# 	print(pd.read_sql_query("SELECT accountNumber, name, Balance FROM bankcustomers", self.connection))


	def searchRecord(self):
		searchingAccountNumber = input("Enter the Account Number do you want to search: ")
		self.cursor.execute("SELECT * FROM bankcustomers WHERE accountNumber = %s" %(searchingAccountNumber))
		record = self.cursor.fetchone()
		print("Account Number: ", record[0])
		print("Customer Name: ", record[1])
		print("Balance: ", record[2])
		if record[3] == 'O':
			print("Status: Account is Active!")
		else:
			print("Status: Account Closed!")

	def updateRecord(self):
		searchingAccountNumber = input("Enter the Account Number do you want to Update: ")
		name = input("Enter the Customer name: ")
		balance = input("Enter the Balance: ")
		self.cursor.execute("UPDATE bankcustomers SET name = '%s', Balance = '%s' WHERE accountNumber = '%s'" %(name, balance, searchingAccountNumber))
		print("\nAccount Updated!")
		print(self.cursor.rowcount)
		self.connection.commit()

	
	def deleteRecord(self):
		searchingAccountNumber = input("Enter the Account Number do you want to delete: ")
		try:
			self.cursor.execute('DELETE FROM bankcustomers WHERE accountNumber = %s' %(searchingAccountNumber))
			self.connection.commit()
		except Exception as error:
			# print("SELECT ErrorDescription FROM Error WHERE ErrorNumber = %s" %(err.sqlstate))
			self.cursor.execute('''SELECT errorDescription FROM error WHERE errorNumber = %s''' %(error.sqlstate))
			deleteMessage = self.cursor.fetchall()
			for message in deleteMessage:
				for msg in message:
					print(msg)
			# print(err.errno)
			# print(err.sqlstate)
			# print("Account Details Deleted Permanently!")



	def exit(self):
		self.connection.close()
		exit()

bank = BankCustomers()

functions = [bank.createRecord, bank.displayRecords, bank.searchRecord, bank.updateRecord, bank.deleteRecord, bank.exit]
while functions != 6:
	functions[int(input("\n1. create a customer\n2. Display all the customers\n3. Search a Record\n4. Update a Record.\n5. Delete Status of a Record\n6. Exit\n\nEnter your choice: "))-1]()


	# def deleteRecord(self):
	# 	searchingAccountNumber = input("Enter the Account Number do you want to delete: ")
	# 	self.cursor.execute("UPDATE bankcustomers SET status = 'C'")
	# 	self.connection.commit()
	# 	print("Account Closed!")


# cursor.execute('UPDATE bankcustomers SET status = \'O\'')
		# connection.commit()