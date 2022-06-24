#Program  to store the function of printOdd and printEven.

numbersList = []
def printOddNumbers():
	for number in range(1, 10, 2):
		print(number)
		numbersList.append(number)
	# print(numbersList)

def printEvenNumbers():
	for number in range(2, 10 + 1, 2):
		print(number)
		numbersList.append(number)
print(numbersList)
