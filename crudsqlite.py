# Cruds Operation Program using Sqlite

import sqlite3
import pandas as pd

class BankCustomers:
	def __init__(self):
		self.connection = sqlite3.connect("bankcustomers.db")
		self.cursor = self.connection.cursor()

	def createRecord(self):
		accountNumber = input("Enter the Account Number: ")
		name = input("Enter the Customer Name: ")
		balance = input("Enter the Balance: ")
		status = 'O'
		self.cursor.execute("""INSERT INTO bankcustomers VALUES (?, ?, ?, ?)""", (accountNumber, name, balance, status))
		print("\nAccount Opened!")
		self.connection.commit()

	# def  displayRecords(self):
	# 	self.cursor.execute("SELECT * FROM bankcustomers")
	# 	bankCustomerRecords = self.cursor.fetchall()
	# 	for record in bankCustomerRecords:
	# 		print("Account Number: ", record[0])
	# 		print("Customer Name: ", record[1])
	# 		print("Balance: ", record[2])
	# 		if record[3] == 'O':
	# 			print("Status: Account is Active!")
	# 		else:
	# 			print("Status: Account Closed!")

	def displayRecords(self):
		# self.cursor.execute("SELECT * FROM bankcustomers")
		# bankCustomerRecords = self.cursor.fetchall()
		# for record in bankCustomerRecords:
		print(pd.read_sql_query("SELECT accountNumber, name, Balance FROM bankcustomers", self.connection))


	def searchRecord(self):
		searchingAccountNumber = input("Enter the Account Number do you want to search: ")
		self.cursor.execute("""SELECT * FROM bankcustomers WHERE accountNumber = ?""", (searchingAccountNumber, ))
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
		self.cursor.execute('''UPDATE bankcustomers SET name = ?, Balance = ? WHERE accountNumber = ?''', (name, balance, searchingAccountNumber, ))
		print("\nAccount Updated!")
		print(self.cursor.rowcount)
		self.connection.commit()

	
	def deleteRecord(self):
		searchingAccountNumber = input("Enter the Account Number do you want to delete: ")
		self.cursor.execute('UPDATE bankcustomers SET status = \'C\'')
		self.connection.commit()
		print("Account Closed!")


	def exit(self):
		self.connection.close()
		exit()

bank = BankCustomers()

functions = [bank.createRecord, bank.displayRecords, bank.searchRecord, bank.updateRecord, bank.deleteRecord, bank.exit]
while functions != 6:
	functions[int(input("\n1. create a customer\n2. Display all the customers\n3. Search a Record\n4. Update a Record.\n5. Delete Status of a Record\n6. Exit\n\nEnter your choice: "))-1]()


# def deleteRecord():
	# 	cursor = connection.cursor()
	# 	searchingAccountNumber = input("Enter the Account Number do you want to delete: ")
	# 	cursor.execute('''DELETE FROM bankcustomers WHERE accountNumber = ?''', (searchingAccountNumber, ))
	# 	connection.commit()
	# 	print("Account Details Deleted Permanently!")


# cursor.execute('UPDATE bankcustomers SET status = \'O\'')
		# connection.commit()