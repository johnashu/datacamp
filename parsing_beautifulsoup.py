import requests
from bs4 import BeautifulSoup 

url = 'https://www.python.org/~guido/'

r = requests.get(url)

html_doc = r.text

soup = BeautifulSoup(html_doc)

pretty_soup = soup.prettify()
print(pretty_soup)

guido_title = soup.title
print(guido_title)

guido_text = soup.get_text()
print(guido_text)

# Import packages
import requests
from bs4 import BeautifulSoup

# Specify url
url = 'https://www.python.org/~guido/'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Extracts the response as html: html_doc
html_doc = r.text

# create a BeautifulSoup object from the HTML: soup
soup = BeautifulSoup(html_doc)

# Print the title of Guido's webpage
print(soup.title)

a_tags = soup.find_all('a')

for link in a_tags:
    print(link.get('href'))
    