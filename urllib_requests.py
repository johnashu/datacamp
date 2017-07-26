from urllib.request import urlopen, Request

url = "http://www.datacamp.com/teach/documentation"

request = Request(url)

response = urlopen(request)

html = response.read()

print(html)

response.close()

import requests

url = "http://docs.datacamp.com/teach/"

r = requests.get(url)

text = r.text
print(text)



