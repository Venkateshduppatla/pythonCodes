# Program for multi threading.

from threading import Thread
from oddandeven import printOddNumbers, printEvenNumbers
# numbersList = []
if __name__ == '__main__':
	thread1 = Thread(target = printOddNumbers)
	thread2 = Thread(target = printEvenNumbers)
	thread1.start()
	thread2.start()
print(numbersList)	