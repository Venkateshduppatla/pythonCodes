# Program  to store the data of BAnk records in csv Format. 

import csv
fields = ['Account Number', 'Name', 'Balance', 'Status']
records = []
bankCustomersDataFile = "sample.csv"
# Function to Load Records from file.

def loadRecords():
	with open (bankCustomersDataFile, "r") as fpBankCustomer:
		csvreader = csv.reader(fpBankCustomer)

# Function to save names into the file.

def saveRecords():
	with open (bankCustomersDataFile, 'w', newline='') as fpBankCustomer:
		csvwriter = csv.writer(fpBankCustomer)
		csvwriter.writerow(fields)
		csvwriter.writerows(records)

# Function to create a record.

def createRecord():
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
 		records.append(record)
 		saveRecords()

# Function to display the records.

def displayRecords():
	for record in records:
		print("\nCustomer Account Number: " + record[0])
		print("Customer Name: " + record[1])
		print("Customer Bank Balance: " + record[2])
		print("Account Status: " + record[3])
		print("\n")

# Function to search a record.

def searchRecord():
	searchTerm = input("Enter the Bank Account Number which you need to be searched: ")
	for record in records:
		if (searchTerm == record[0]):
			print("Record Found!\n")
			print("\nCustomer Account Number: " + record[0])
			print("Customer Name: " + record[1])
			print("Customer Balance: " + record[2])
			print("Account Status: " + record[3])
			print("\n")
			break

# Function to update a record.

def updateRecord():
	searchTerm = input("Enter the Bank Account Number of customer which you need to be updated: ")
	for record in records:
		if (searchTerm == record[0]):
	 		customerName = input("Enter the name of the Customer: ")
	 		record[1] = customerName
	 		bankBalance = input("Enter the Bank Balance: ")
	 		record[2] = bankBalance
	 		saveRecords()
	 		print("\nRecord Updated!\n")
	 		break
	 		
#Function to show delete status of a record.

def deleteRecord():
	searchTerm =input("Enter the Bank Account Number which you need to close: ")
	for record in records:
		if (searchTerm == record[0]):
			status = 'Closed!'
			record[3] = status
			saveRecords()
			print("\nBank Account is Closed!\n")
			break

# Show Menu.

choice = 0
while (choice != 6):
	loadRecords()
	functions = [createRecord, displayRecords, searchRecord, updateRecord, deleteRecord, exit]
	choice = int(input("\n1. create a customer\n2. Display all the customer\n3. Search a Record\n4. Update a Record.\n5. Close a Record\n6. Exit\n\nEnter your choice: "))
	functions[choice - 1]()

# Function to Exit. 

def exit():
	exit()