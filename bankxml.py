# Program to store the records in xml format.

from xml.dom import minidom
import os
import xml.etree.ElementTree as gfg
bankRecordsDataFile = "bankcustomer.xml"



class Bank():
	# def __init__(self):
	# 	self.root = gfg.Element('BankRecords')

	def saveRecord(self):
		self.tree = gfg.ElementTree(self.root)
		with open(bankRecordsDataFile, "wb") as fpBankCustomer:
			self.tree.write(fpBankCustomer)	

	def loadRecords(self):
		tree = gfg.parse(bankRecordsDataFile)
		self.root = tree.getroot()
		
	def createRecord(self):
		self.h1 = gfg.Element('Record')
		self.root.append(self.h1)


		self.h1 = gfg.SubElement(self.root, 'Record')

		self.a1 = gfg.SubElement(self.h1, 'AccountNumber')
		self.a1.text = input("Enter the Account Number: ")

		self.a2 = gfg.SubElement(self.h1, 'Name')
		self.a2.text = input("Enter the Name: ")

		self.a3 = gfg.SubElement(self.h1, 'Balance')
		self.a3.text = input("Enter the Bank Balance: ")

		self.a4 = gfg.SubElement(self.h1, 'Status')
		self.a4.text = 'O'
		print("\nBank Account Opened!")
		self.saveRecord()

	# def displayRecords(self):
	# 	for record in self.root:
	# 		for SubElement in record:
	# 			if SubElement.tag != 'Status':
	# 				print(SubElement.tag + ": " + SubElement.text)
	# 			else:
	# 				if SubElement.text == 'O':
	# 					print(SubElement.tag + ": Opened!")	
	# 				else:	
	# 					print(SubElement.tag + ": Closed!")

	def displayRecords(self):
		for record in self.root:
			if record[3].text == 'O':
				for fieldValueCounter in range(0, 3):
					print(record[fieldValueCounter].tag + ": " + record[fieldValueCounter].text)

	
	def searchRecord(self):
		searchedTerm = input("Enter the Account Number do you want the  details: ")
		for record in self.root:
			for SubElement in record:
				if SubElement.text == searchedTerm:
					for SubElement in record:
						if SubElement.tag != 'Status':
							print(SubElement.tag + ": " + SubElement.text)
						else:
							if SubElement.text == 'O':
								print(SubElement.tag + ": Opened!")	
							else:	
								print(SubElement.tag + ": Closed!")	
				break
	
	def updateRecord(self):
		searchedTerm = input("Enter the Account Number do you want the  details: ")
		for record in self.root:
			for SubElement in record:
				if searchedTerm == SubElement.text:
					for SubElement in record:
						if SubElement.tag != 'Status':
							if SubElement.tag != "AccountNumber":
								SubElement.text = input(SubElement.tag + ": ")
							self.saveRecord()
					print("\nRecord Updated!")
	
	def deleteStatus(self):
		searchedTerm = input("Enter the Account Number do you want the  details: ")
		for record in self.root:
			for SubElement in record:
				if searchedTerm == SubElement.text:
					for SubElement in record:
						if SubElement.tag == "Status":
							SubElement.text = 'C'
							self.saveRecord()
					print("Account Closed!\n")
							

	def exit(self):
		print("\nSession Ended!")
		quit()
g = Bank()

functions = [g.createRecord, g.displayRecords, g.searchRecord, g.updateRecord, g.deleteStatus, g.exit]
while functions != 6:
	g.loadRecords()
	functions[int(input("\n1. create a customer\n2. Display all the customers\n3. Search a Record\n4. Update a Record.\n5. Close a Record\n6. Exit\n\nEnter your choice: "))-1]()
