# Main program of CRUD frameworks using classes.

from crudwithclass import*
bank = BankCustomers()
choice = 0
while (choice != 6):
	bank.loadRecords()
	functions = [bank.createRecord, bank.displayRecords, bank.searchRecord, bank.updateRecord, bank.deleteRecord, bank.exit]
	choice = int(input("\n1. create a customer\n2. Display all the customer\n3. Search a Record\n4. Update a Record.\n5. Close a Record\n6. Exit\n\nEnter your choice: "))
	functions[choice - 1]()