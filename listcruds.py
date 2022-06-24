# Program on cruds operation to store data in dictionaries as key is ID and values in the form of List. 

records = {}
bankCustomersDataFile = "dicbankrecords.dat"
# Function to Load Records from file.

def loadRecords():
	global records
	with open (bankCustomersDataFile, "r") as fpBankCustomer:
		records = eval(fpBankCustomer.read())

# Function to save names into the file.

def saveRecords():
	with open (bankCustomersDataFile, "w") as fpBankCustomer:
		fpBankCustomer.write(str(records))

# Function to create a record.

def createRecord():
	record = []
	accountNumber = input("Enter the Account Number: ")
	record.append(input("Enter the Customer Name: "))
	record.append(input("Enter the Balance: "))
	record.append("O")
	records[accountNumber] = record


# Function to display all the records.

def displayRecords():
	for field, fieldValue in records.items():
		print("\n")
		print("Account Number:", field)
		print("Customer Name:", fieldValue[0])
		print("Bank Balance:", fieldValue[1])
		print("Account Opened!\n")
		if fieldValue[2] == "O":
			print("Account Status: Opened!")
		else:
			print("Account Status: Closed!")
# Function to search record. 

def searchRecord():
 	searchTerm = input("Enter the account to which do you need details: ")
 	for field, fieldValue in records.items():
 		if (searchTerm == field):
 			print("Account Number:", field)
 			print("Customer Name:", fieldValue[0])
 			print("Bank Balance:", fieldValue[1])
 			if fieldValue[2] == "O":
 				print("Account Status: Opened!")
 			else:
 				print("Account Status: Closed!")	
 			break


# Function to update a record. 

def updateRecord():
	searchTerm = input("Enter the account to which do you need details: ")
	for field, fieldValue in records.items():
		if (searchTerm == field):
			fieldValue[0] = input("Enter the Customer Name: ")
			fieldValue[1] = (input("Enter the Balance: "))
			saveRecords()
			print("\nRecord Updated!\n")
			break

# Function to delete a record. 

def deleteRecord():
	searchTerm = input("Enter the account to which do you need details: ")
	for field, fieldValue in records.items():
		if (searchTerm == field):
			status = input("\nDo you want to close the account for sure\nPress y to close: ")
			if status == "y":
				fieldValue[2] = ("C")
				saveRecords()
				print("\nAccount Closed!")
			break
choice = 0
loadRecords()
while (choice != 6):
	functions = [createRecord, displayRecords, searchRecord, updateRecord, deleteRecord, exit]
	choice = int(input("\n1. create a customer\n2. Display all the customer\n3. Search a Record\n4. Update a Record.\n5. Close a Record\n6. Exit\n\nEnter your choice: "))
	functions[choice - 1]()

# Function to Exit. 

def exit():
	exit()		