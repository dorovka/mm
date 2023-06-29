import requests
import json

url = "https://swapi.dev/api/"
response = requests.get(url).json()
url_people = response.get("people")
def check_people(url):
    for i in range(1, 4):
        response = requests.get(f"{url}/{i}").json()
        print(response.get("name"))


url_planets = response.get("planets")
def check_planets(url):
    diameter = {}
    for i in range(1, 6):
        response = requests.get(f"{url}/{i}").json()
        diameter[response.get("name")] = response.get("diameter")
    print(diameter)
check_people(url_people)
check_planets(url_planets)