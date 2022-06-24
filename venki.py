
from threading import Thread
numbersList = []
def printOddNumbers():
	for number in range(1, 10, 2):
		print(number)
		numbersList.append(number)
	print(numbersList)

def printEvenNumbers():
	for number in range(2, 10 + 1, 2):
		print(number)
		numbersList.append(number)
	print(numbersList)

if __name__ == '__main__':
	process1 = Thread(target = printOddNumbers)
	process2 = Thread(target = printEvenNumbers)
	process1.start()
	process2.start()
print(numbersList)
# print("Odd Numbers are")
# printOddNumbers()
# print("Even Numbers are")
# printEvenNumbers()