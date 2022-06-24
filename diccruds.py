# Cruds program to save the data in the dictionaries within the list.

records = []
bankCustomersDataFile = "bankdata.dat"
# Function to load records from file.

def loadRecords():
	global records
	with open (bankCustomersDataFile, "r") as fpBankCustomers:
		records = eval(fpBankCustomers.read())

# Function to save records into the file.
def saveRecords():
	with open (bankCustomersDataFile, "w") as fpBankCustomer:
		fpBankCustomer.write(str(records))


#Function to create a record.

def createRecord():
	record = {}
	record['Account Number'] = input("Enter the Account Number: ")
	record['Customer Name'] = input("Enter the Customer Name: ")
	record['Bank Balance'] = input("Enter the Bank Balance: ")
	record['Status'] = "Opened"
	records.append(record)
	saveRecords()

# Function to display all the records.

def displayRecords():
	for record in records:
		for field, fieldValue in record.items():
			print(field + ":" + fieldValue)

# Function to search record. 

def searchRecord():
 	searchTerm = input("Enter the account to which do you need details: ")
 	for record in records:
 		if (searchTerm == record['Account Number']):
 	 		for field, fieldValue in record.items():
 	 			print(field + ":" + fieldValue)


# Function to update a record. 

def updateRecord():
	searchTerm = input("Enter the account to which do you need details: ")
	for record in records:
		if (searchTerm == record['Account Number']):
	 		for field, fieldValue in record.items():
	 			record['Customer Name'] = input("Enter the Customer Name: ")
	 			record['Bank Balance'] = input("Enter the Bank Balance: ")
	 			saveRecords()
	 			print("\nRecord Updated!\n")
	 			break

# Function to delete a record. 

def deleteRecord():
	searchTerm = input("Enter the account to which do you need details: ")
	for record in records:
		if (searchTerm == record['Account Number']):
			record['Status'] = 'Closed'
			saveRecords()
			print("\nRecord Deleted!\n")
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