# Framework Program on cruds operation. 

import sqlite3
import pandas as pd
menuFile = "menulines.cfg"
fieldNames = []
connection = sqlite3.connect("frameworkdata.db")
cursor = connection.cursor()
cursor.execute("PRAGMA table_info(frameWorks);")
fieldNamesinTuple = cursor.fetchall()
for fieldName in fieldNamesinTuple:
	fieldNames.append(fieldName[1])

def loadMenu():
	global menu
	with open(menuFile, 'r') as fpMenuLines:
		menu = fpMenuLines.read()


def createRecord():
	fieldValue = []
	for fieldName in fieldNames[:len(fieldNames)-1]:
		fieldValue.append(input("Enter the " + fieldName + ": "))
	fieldValue.append("0")
	cursor.execute("INSERT INTO frameWorks VALUES " + str(tuple(fieldValue)))
	connection.commit()

def displayallRecords():
	choice = input("In which Style do you want the  data  to e  printed\n1. Form Style\n2. Tablular style\nEnter your Choice: ")
	if choice == '1':
		cursor.execute("SELECT * FROM frameWorks")
		records = cursor.fetchall()
		for record in records:
			fieldValueCounter = 0
			print("")		
			if record[len(fieldNames)-1] == '0':
				for fieldName in fieldNames[:len(fieldNames)-1]:
					print(fieldName, ":", record[fieldValueCounter])
					fieldValueCounter += 1
	else:
		print(pd.read_sql_query("SELECT * FROM frameWorks", connection))

def searchRecord():
	try:
		searchingTerm = input("Enter the " + fieldNames[0] + ": ")
		cursor.execute("SELECT * FROM frameWorks WHERE %s = %s" %(fieldNames[0], searchingTerm))
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
		cursor.execute("UPDATE frameWorks SET %s = '%s' WHERE %s = %s" %(fieldName, fieldValue, fieldNames[0], searchingTerm))
		connection.commit()

def deleteRecord():
	searchingTerm = input("Enter the " + fieldNames[0] + ": ")
	cursor.execute("UPDATE frameWorks SET %s = \"1\" WHERE %s = %s" %(fieldNames[-1], fieldNames[0], searchingTerm))
	connection.commit()


def exit():
	connection.close()
	quit()

functions = [createRecord, displayallRecords, searchRecord, updateRecord, deleteRecord, exit]
loadMenu()
while functions != 6:
	functions[int(input(menu))-1]()


