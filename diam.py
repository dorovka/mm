import requests
import json
sendto = ''
url = "https://swapi.dev/api/"
response = requests.get(url).json()
maximum = []

url_starships = response.get('planets')
def Starships(url):
    global sendto
    for i in range(1, 61):
        response = requests.get(f"{url}/{i}").json()
        check = str(response.get("diameter"))[0]
        if any(c.isalpha() for c in check) == False:
            maximum.append(int(response.get("diameter")))
        else:
            pass
    sendto = "максимальный диаметр: " + str(max(maximum))
    return sendto

maximum2 = []

url_starships2 = response.get('starships')
def Starships2(url):
    ships = {}
    for i in range(0, 70):
        response = requests.get(f"{url}/{i}").json()
        check = str(response.get("max_atmosphering_speed"))[0]
        check2 = str(response.get("max_atmosphering_speed"))[-1]
        if check == "1" or check == '2' or check == '3' or check == '4' or check == '5' or check == '6' or check == '7' or check == '8' or check == '9':
            if check2 != 'm':
                ships[response.get("max_atmosphering_speed")] = response.get("name")
                maximum2.append(int(response.get("max_atmosphering_speed")))
            else:
                pass
    max_speed = str(max(maximum2))
    name = ships[max_speed]
    sendto2 = f'Корабль {name} имеет наибольшую скорость: {max_speed}'
    return sendto2