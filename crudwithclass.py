# Program with functions to run cruds operation using Classes.

bankCustomersDataFile = "bankrecords.dat"
class BankCustomers:
	def __init__(self):
		self.records = []
	# Function to Load Records from file.

	def loadRecords(self):
		with open (bankCustomersDataFile, "r") as fpBankCustomer:
			self.records = eval(fpBankCustomer.read())

	# Function to save names into the file.

	def saveRecords(self):
		with open (bankCustomersDataFile, "w") as fpBankCustomer:
			fpBankCustomer.write(str(self.records))


	# Function to create a record.

	def createRecord(self):
	 		record = []
	 		accountNumber = input("Enter the Account Number: ")
	 		record.append(accountNumber)
	 		customerName = input("Enter the name of the Customer: ")
	 		record.append(customerName)
	 		bankBalance = input("Enter the Bank Balance: ")
	 		record.append(bankBalance)
	 		status = 'Opened!'
	 		print("\nBank Account Opened!\n")
		 	record.append(status)
	 		self.records.append(record)
	 		self.saveRecords()

	# Function to display the records.

	def displayRecords(self):
		
		for record in self.records:
			print("\nCustomer Account Number: " + record[0])
			print("Customer Name: " + record[1])
			print("Customer Bank Balance: " + record[2])
			print("Account Status: " + record[3])
			print("\n")

	# Function to search a record.

	def searchRecord(self):
		searchTerm = input("Enter the Bank Account Number which you need to be searched: ")
		for record in self.records:
			if (searchTerm == record[0]):
				print("Record Found!\n")
				print("\nCustomer Account Number: " + record[0])
				print("Customer Name: " + record[1])
				print("Customer Balance: " + record[2])
				print("Account Status: " + record[3])
				print("\n")
				break

	# Function to update a record.

	def updateRecord(self):
		searchTerm = input("Enter the Bank Account Number of customer which you need to be updated: ")
		for record in self.records:
			if (searchTerm == record[0]):
		 		customerName = input("Enter the name of the Customer: ")
		 		record[1] = customerName
		 		bankBalance = input("Enter the Bank Balance: ")
		 		record[2] = bankBalance
		 		self.saveRecords()
		 		print("\nRecord Updated!\n")
		 		break
		 		
	#Function to show delete status of a record.

	def deleteRecord(self):
		searchTerm =input("Enter the Bank Account Number which you need to close: ")
		for record in self.records:
			if (searchTerm == record[0]):
				status = 'Closed!'
				record[3] = status
				self.saveRecords()
				print("\nBank Account is Closed!\n")
				break

	# Function to Exit. 

	def exit():
		exit()	

