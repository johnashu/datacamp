import requests

url = 'http://www.omdbapi.com/?apikey=ff21610b&t=social+network'

r =requests.get(url)

json_data = r.json()

for k in json_data.keys():
    print(k + ': ', json_data[k])

