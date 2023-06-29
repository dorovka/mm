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