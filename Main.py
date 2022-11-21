import requests

URL = "https://swapi.dev/api/people/4"
response = requests.get(URL, timeout=5)
jsonObject = response.json()
field = jsonObject["name"]
print(field)
