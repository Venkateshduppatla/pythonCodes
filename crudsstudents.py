studentRecords = []
studentsDataFile = "studentrecords.dat"

# Function to Load records From File. 

def loadRecords():
	global studentRecords
	with open(studentsDataFile, "r") as fpStudentRecords:
		studentRecords = eval(fpStudentRecords.read())

#Function to Save Record

def saveRecords():
	with open(studentsDataFile, "w") as fpStudentRecords:
		fpStudentRecords.write(str(studentRecords))

# Function to create a record. 
def createStudentRecord():
	studentRecord = []
	rollNumber = input("Enter the Roll Number: ")
	studentRecord.append(rollNumber)
	studentName = input("Enter the name of the student: ")
	studentRecord.append(studentName)
	studentAadharNumber = input("Enter the Aadhar Number of the student: ")
	studentRecord.append(studentAadharNumber)
	studentFatherName = input("Enter the Father Name of the student: ")
	studentRecord.append(studentFatherName)
	parentPhoneNumber = input("Enter the Phone Number of the Parent: ")
	studentRecord.append(parentPhoneNumber)
	status = "Pursuing"
	studentRecord.append(status)
	studentRecords.append(studentRecord)
	saveRecords()

# Function to display all the records.

def displayStudentRecords():
	for studentRecord in studentRecords:
		print("Roll Number of the Student: " + studentRecord[0])
		print("Name of the Student: " + studentRecord[1])
		print("Aadhar Number of the Student: " + studentRecord[2])
		print("Father Name of the Student: " + studentRecord[3])
		print(" Phone Number of the Parent: " + studentRecord[4])
		print("Status of the Student: " + studentRecord[5] + "!")

# Function to Search a Student Record.

def searchStudent():
	searchTerm = input("Enter the Roll Number of the student to which you need details: ")
	for studentRecord in studentRecords:
		if (searchTerm == studentRecord[0]):
			print("Roll Number of the Student: " + studentRecord[0])
			print("Name of the Student: " + studentRecord[1])
			print("Aadhar Number of the Student: " + studentRecord[2])
			print("Father Name of the Student: " + studentRecord[3])
			print(" Phone Number of the Parent: " + studentRecord[4])
			print("Status of the Student: " + studentRecord[5] + "!")
			break

# Function to update a student Record. 

def updateStudentRecord():
	searchTerm = input("Enter the Roll Number of the student to which you need to update: ")
	for studentRecord in studentRecords:
		if (searchTerm == studentRecord[0]):
			studentName = input("Enter the name of the student: ")
			studentRecord[1] = studentName
			parentPhoneNumber = input("Enter the Phone Number of the Parent: ")
			studentRecord[4] = parentPhoneNumber
			saveRecords()
			break

#Function to delete a student record.

def statusOfRecord():
	searchTerm = input("Enter the Roll Number of the student to which you need to update: ")
	for studentRecord in studentRecords:
		if (searchTerm == studentRecord[0]):
			status = "Relieved"
			studentRecord[5] = status
			saveRecords()
			print("Student Status Updated!\n")
			break

# Show Menu. 

choice = 0

while (choice != 6):
	loadRecords()
	functions = [createStudentRecord, displayStudentRecords, searchStudent, updateStudentRecord, statusOfRecord, exit]
	choice = int(input("\n1. Create a Student Record\n2. Display all the students\n3. Search for a Student Record\n4. Update a Student record\n5. Status of a Student Record\n6. Exit\n\nEnter your Choice: "))
	functions[choice - 1]()

#Function to exit.

def exit():
	exit()

