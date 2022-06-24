# import googlemaps
# import os

# def run():
# 	apiKey = os.environ['AIzaSyDwmS_CJ-OLo9nyQDTTVI5HW7oO8-dV410']
# 	gmapsClient = googlemaps.Client(apiKey)
# 	geocodeResult = gmapsClient.geocode('1600.Amphitheatre.Parkway,-Mountain-View,-CA')
# 	result = geocodeResult[0]
# 	print(result)
# 	# print('Address: ', result['formatted_address'])
# 	# print('Latitude: ', result['geometry']['location']['lat'])
# 	# print('Longitude: ', result['geometry']['location']['lon'])

# if __name__ == "__main__":
# 	run()

# import requests
# apiKey = "AIzaSyDwmS_CJ-OLo9nyQDTTVI5HW7oO8-dV410"
# url = "https://maps.googleapis.com/maps/api/staticmap?"
# location = input("Enter the location: ")
# zoom = 10
# r = requests.get(url + "center=" + location + "&zoom" + str(zoom) + "&size=1024x786&key=" + apiKey)
# print(url + "center=" + location + "&zoom" + str(zoom) + "&size=1024x786&key" + apiKey)
# urlForTemperature = eval(requests.get("https://api.openweathermap.org/data/2.5/weather?q=" + location + "&units=metric&appid=3bd3cf90bdd0e58f6460e8280d878c9a").text)
# print("https://api.openweathermap.org/data/2.5/weather?q=" + location + "&units=metric&appid=3bd3cf90bdd0e58f6460e8280d878c9a")
# print(urlForTemperature)
# f = open('D:/training/python/maps3.ping', 'wb')
# f.write(r.content)
# f.close()

# import requests
# from tkinter import * 
# from tkintermapview import TkinterMapView

# rootTk = Tk()
# rootTk.geometry(f"{600}x{400}")
# rootTk.title("Map")
# def left_click_event(coordinates):
# 	global temperatureEntry
# 	temperatureEntry.destroy()
# 	latitude = coordinates[0]
# 	longitude = coordinates[1]
# 	mapWindow.set_position(latitude, longitude)
# 	urlForTemperature = eval(requests.get("https://api.openweathermap.org/data/2.5/weather?lat=" + str(latitude) + "&lon=" + str(longitude) + "&units=metric&appid=3bd3cf90bdd0e58f6460e8280d878c9a").text)['main']['temp']
# 	temperatureEntry = Label(rootTk, text = urlForTemperature, fg = 'black', bg = 'white')
# 	temperatureEntry.place(relheight= 0.09, rely = 0.9, relx = 0.2)

# mapWindow = TkinterMapView(rootTk, width=600, height=1200, corner_radius=0)
# mapWindow.place(relx = 0.02, rely = 0.01, relheight = 0.9, relwidth = 0.97)
# mapWindow.set_address("India")
# mapWindow.add_left_click_map_command(left_click_event)
# temperatureLabel = Label(rootTk, text = "Temperature: ")
# temperatureLabel.place(relheight= 0.09, relwidth = 0.2, rely = 0.9, relx = 0)
# temperatureEntry = Label(rootTk, text = " ", bg = 'white')
# temperatureEntry.place(relheight= 0.09, rely = 0.9, relx = 0.2)


# rootTk.mainloop()

# Program to display the map along with the temperature. 

from tkinter import *
from tkintermapview import TkinterMapView
import requests

root_tk = Tk()
root_tk.geometry(f"{600}x{400}")
root_tk.title("Map")

tempLabel = Label(root_tk, text = "Temperature", font = "Helvetica 14 bold")
tempLabel.place(relx = 0.02, relheight = 0.05, relwidth = 0.2)

# create map widget
map_widget = TkinterMapView(root_tk, width=600, height=1200, corner_radius=0)
map_widget.place(relx = 0.02, rely = 0.06, relheight = 0.8, relwidth = 0.97)

map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)

map_widget.set_address("India")

def left_click_event(coordinates_tuple):
	latValue = coordinates_tuple[0]
	longValue = coordinates_tuple[1]
	print("Left click event with coordinates:", coordinates_tuple)
	temperatureOfCity = eval(requests.get("https://api.openweathermap.org/data/2.5/weather?lat=" + str(latValue) + "&lon=" + str(longValue) + "&appid=0a3ef48eb27734ca0632f59111180451&units=metric").text)['main']['temp']
	tempValue = Label(root_tk, text = temperatureOfCity)
	tempValue.place(relx = 0.23, relheight = 0.05, relwidth = 0.2)
    
map_widget.add_left_click_map_command(left_click_event)

root_tk.mainloop()