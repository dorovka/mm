import requests
import json

url = "https://swapi.dev/api/"
response = requests.get(url).json()
maximum = []

url_starships = response.get('starships')
def Starships(url):
    for i in range(58, 70):
        response = requests.get(f"{url}/{i}").json()
        check = str(response.get("max_atmosphering_speed"))[0]
        if check == "1" or check == '2' or check == '3' or check == '4' or check == '5' or check == '6' or check == '7' or check == '8' or check == '9':
            maximum.append(int(response.get("max_atmosphering_speed")))
        else:
            pass
        print(response.get("max_atmosphering_speed"))
    print("максимальная скорость: " + str(max(maximum)))
Starships(url_starships)