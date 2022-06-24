# Program to print sum of two numbers.

#print("sum of", (number1 := int(input("Enter the number-1: "))), "and", (number2 := int(input("Enter the number-2: "))), "is", (number1 + number2))

# Program to print Natural Numbers between Range. 

# for number in range(int(input("Enter the starting natural number do yout want the list:")), int(input("Enter the end natural number do yout want the list: ")) + 1):
# 	print(number)
	
# Program to find the weather of a particular city.

# import requests
# print("The Temperature at ", (cityName := input("Enter the City Name do you need temperature: ")), " is ", (eval(requests.get("https://api.openweathermap.org/data/2.5/weather?q=" + cityName + "&units=metric&appid=3bd3cf90bdd0e58f6460e8280d878c9a").text) ['main']['temp']), ".")

# program to find whehter the given number is prime number or not.

# primeStatus = 1
# factor = 2
# number = eval(input("Enter the  number do you want to check prime or not: "))
# if number < factor:
# 	print(number + " is neither prime nor composite.")
# elif number == factor:
# 	primeStatus = 1
# elif number == factor + 1:
# 	primeStatus = 1
# elif number % factor == 0:
# 	primeStatus = 0
# else:
# 	for factor in range(3, int(number**0.5)+2, 2):
# 		if number % factor == 0:
# 			primeStatus = 0
# if primeStatus == 0:
# 	print(str(number) + " is a composite number.")
# else:
# 	print(str(number) + " is a prime number.")

	
			



# Program to find the meaning of a word. 

import requests
import vlc
#print("The meaning of ", word := input("Enter the word do you need meaning: "), " is ", "\"", str(eval(requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/" + word).text)[0] ['meanings'][0]['definitions'][0]['definition']), "\"")
print("The meaning of ", word := input("Enter the word do you need meaning: "), " is ", "\"", str(eval(requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/" + word).text)[0]['phonetics'][0]['audio']), "\"")
media = vlc.MediaPlayer(str(eval(requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/" + word).text)[0]['phonetics'][0]['audio']))
media.play()
input("\nEnter any key to Exit!")
# Program to recognizze audio and print the text. 
#https://api.dictionaryapi.dev/media/pronunciations/en/read-1-us.ogg