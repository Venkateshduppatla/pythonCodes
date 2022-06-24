# Frame Work Program. 

records = []
menu = []
fields = []
menuLines = "menulines.cfg"
fieldNames = "crudfieldnames.cfg"
dataFile = "crudsframework.dat"

# Function to load menu lines.

def loadMenuLines():
	global menu
	menu = open(menuLines, "r").read()

# Function to load field names.

def loadFieldNames():
	global fields
	fields = eval(open(fieldNames, "r").read())

#Function to load records.

def loadRecords():
	global records
	records = eval(open(dataFile, "r").read())

# Function to save records.

def saveRecords():
	open(dataFile, "w").write(str(records))

# Function to Create a record.

def createRecord():
	record = []
	for field in fields[0:-1]:
		fieldValue = input("Enter the " + field + ": ")
		record.append(fieldValue)
	record.append("Not Paid!")
	records.append(record)
	saveRecords()

# Function to Display all the records.

def displayRecords():
	for record in records:
		recordCounter = 0
		for field in fields:
			print(field + ": " + record[recordCounter])
			recordCounter += 1
		print()	

# Function to search for a record.

def searchRecord():
	searchTerm = input("\nEnter the " + fields[0] + " do you need to search: ")
	for record in records:
		if searchTerm == record[0]:
			recordCounter = 0
			print("\nRecord Found!\n")
			for field in fields:
				print(field + ": " + record[recordCounter])
				recordCounter += 1
			break
# Function to update a record. 

def updateRecord():
	searchTerm = input("\nEnter the " + fields[0] + " do you need to update: ")
	for record in records:
		if searchTerm == record[0]:
			recordCounter = 1
			for field in fields[1:]:
				fieldValue = input("Enter the " + field + ": ")
				record[recordCounter] = fieldValue
				recordCounter += 1
			break
			saveRecords()
			print("\nRecord Updated!\n")

# Function to delete a record. 

def deleteRecord():
	searchTerm = input("\nEnter the " + fields[0] + " do you need to search: ")
	for record in records:
		if searchTerm == record[0]:
			status = input("Do you want to close the record\npress 'y' for yes: ")
			if status == "y":
				record[-1] = "Paid!"
				saveRecords()	
			break	

# Show Menu.

choice = 0
loadMenuLines()
loadFieldNames()
loadRecords()
functions = [createRecord, displayRecords , searchRecord, updateRecord, deleteRecord, exit]
while choice != 6:
	choice = int(input("\n" + menu))
	functions[choice -1]()


#Function to exit.

def exit():
	exit()

