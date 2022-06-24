# Cruds program to save the data in the dictionaries within the list.

import xml.etree.ElementTree as gfg
records = []
bankCustomersDataFile = "bankcustomers.xml"
# Function to load records from file.

def loadRecords():
	global records
	record = {}
	tree = gfg.parse(bankRecordsDataFile)
	records = tree.getroot()
	for record in root:
		for SubElement in record:
			record[SubElement.tag] = SubElement.text
		records.append(record)


# Function to save records into the file.
def saveRecords():
	root = gfg.Element('records')
	for record in records:
		element = gfg.SubElement(root, 'record')
		# element = gfg.Element('record')
		# root.append(element)
		for field, fieldValue in record.items():
			subElement = gfg.SubElement(element, field)
			subElement.text = fieldValue

	tree = gfg.ElementTree(root)
	with open(bankRecordsDataFile, "wb") as fpBankCustomer:
		tree.write(fpBankCustomer)	


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