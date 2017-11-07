import urllib.request
from bs4 import BeautifulSoup

html = urllib.request.urlopen('https://en.wikipedia.org/wiki/List_of_programming_languages')
soup = BeautifulSoup(html,'html.parser')
print(soup.title)