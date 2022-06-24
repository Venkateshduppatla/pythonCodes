import pyaudio
import pyttsx3
import requests
import speech_recognition as sr
with sr.Microphone() as source:
	r = sr.Recognizer()
	voiceInput = r.listen(source)
	voiceInput = r.recognize_google(voiceInput)
	#print("You Said:", voiceInput := r.recognize_google(voiceInput))
if str(voiceInput) == "need temperature":
	with sr.Microphone() as source:
		r.adjust_for_ambient_noise(source)
		print("Say Some Thing...")
		cityName = r.listen(source)
		print("You Said:", cityName := r.recognize_google(cityName))
		
	cityTemperature = pyttsx3.init()
	cityTemperature.say("The temperature at " + cityName + "is " + str(eval(requests.get("https://api.openweathermap.org/data/2.5/weather?q=" + cityName + "&units=metric&appid=3bd3cf90bdd0e58f6460e8280d878c9a").text) ['main']['temp']))
	cityTemperature.runAndWait()
	cityTemperature.stop()