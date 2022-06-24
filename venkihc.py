
# enteredText = input("Enter: ")
# def cleanInput():
# 	userInput = enteredText.replace("'", "''")
# 	return userInput
# data = cleanInput(enteredText)
# print(data)

# Program to run a sqlite command prompt.

# import sqlite3

# connection = sqlite3.connect("frameworkdata-2.db")
# cursor = connection.cursor()
# while 1:
# 	try:
# 		userInput = input("sqlite>>>")
# 		if userInput == 'exit':
# 			connection.close()
# 			break	
# 			quit()
# 		cursor.execute(userInput)
# 		records = cursor.fetchall()
# 		for record in records:
# 			print(record)
# 		connection.commit()
# 	except:
# 		print("Error!")

import sqlite3

while 1:
	try:
		userInput = input("sqlite>>>")
		fileName = userInput.split(" ")
		if ".open" in userInput:
			connection = sqlite3.connect(fileName[1])
			cursor = connection.cursor()
		elif userInput == 'exit':
			connection.close()
			quit()
		else:
			cursor.execute(userInput)
			records = cursor.fetchall()
			for record in records:
				print("|".join(map(str, record)))
			connection.commit()
	except Exception as error:
		print(error)