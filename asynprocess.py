# Program for multiprocessing. 

from multiprocessing import Process
from oddandeven import printOddNumbers, printEvenNumbers
# numbersList = []
if __name__ == '__main__':
	process1 = Process(target = printOddNumbers)
	process2 = Process(target = printEvenNumbers)
	process1.start()
	process2.start()
print(numbersList)