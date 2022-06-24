# Framework Program of Cruds using sqlite.

import sqlite3
import pandas as pd
menuFile = "menulines.cfg"
fieldNames = []
connection = sqlite3.connect("frameworkdata-2.db")
cursor = connection.cursor()
cursor.execute("PRAGMA table_info(framework);")
fieldNamesinTuple = cursor.fetchall()
for fieldName in fieldNamesinTuple:
	fieldNames.append(fieldName[1])

def cleanInput(text):
	text = text.replace("'", "''")
	return text

def loadMenu():
	global menu
	with open(menuFile, 'r') as fpMenuLines:
		menu = fpMenuLines.read()

def createRecord():
	fieldValue = []
	for fieldName in fieldNames[:len(fieldNames)-1]:
		fieldValue.append(input("Enter the " + fieldName + ": "))
	fieldValue.append("0")
	cursor.execute("INSERT INTO framework VALUES " + str(tuple(fieldValue)))
	connection.commit()

def displayRecords():
	choice = input("In which Style do you want the  data  to be  printed\n1. Form Style\n2. Tabular style\nEnter your Choice: ")
	if choice == '1':
		cursor.execute("SELECT * FROM framework")
		records = cursor.fetchall()
		for record in records:
			fieldValueCounter = 0
			if record[len(fieldNames)-1] == '0':
				print("")
				for fieldName in fieldNames[:len(fieldNames)-1]:
					print(fieldName, ":", record[fieldValueCounter])
					fieldValueCounter += 1
		print("")
	else:
		print(pd.read_sql_query("SELECT * FROM framework", connection))

def searchRecord():
	try:
		searchingTerm = input("Enter the " + fieldNames[0] + ": ")
		cursor.execute("SELECT * FROM framework WHERE %s = %s" %(fieldNames[0], searchingTerm))
		record = cursor.fetchone()
		fieldValueCounter = 0
		print("")		
		for fieldName in fieldNames[:len(fieldNames)-1]:
			print(fieldName, ": ", record[fieldValueCounter])
			fieldValueCounter += 1
	except:
		print("No Record Found!")


def updateRecord():
	searchingTerm = input("Enter the " + fieldNames[0] + ": ")
	for fieldName in fieldNames[1 : len(fieldNames)-1]:
		fieldValue = (input("Enter the " + fieldName + ": "))
		fieldValue = cleanInput(fieldValue)
		cursor.execute("UPDATE framework SET %s = '%s' WHERE %s = %s" %(fieldName, fieldValue, fieldNames[0], searchingTerm))
		connection.commit()
	updateStatus = cursor.rowcount
	if updateStatus == 0:
		print("No Record Updated!")

def recordStatus():
	searchingTerm = input("Enter the " + fieldNames[0] + ": ")
	cursor.execute("UPDATE framework SET %s = \"1\" WHERE %s = %s" %(fieldNames[-1], fieldNames[0], searchingTerm))
	connection.commit()
	status = cursor.rowcount
	if status == 0:
		print("\nNo Record Found!\n")

def exit():
	print("Session Ended!")
	quit()
functions =[createRecord, displayRecords, searchRecord, updateRecord, recordStatus, exit]
while (functions != 6):
	loadMenu()
	functions[int(input(menu))-1]()