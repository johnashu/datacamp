import requests

url = 'https://en.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&exintro=&titles=pizza'

r = requests.get(url)

json_data = r.json()

pizza_extract = json_data['query']['pages']['24768']['extract']
print(pizza_extract)

