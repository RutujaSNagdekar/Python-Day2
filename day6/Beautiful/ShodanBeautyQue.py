#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup as bb


query=input("Enter search query:")

url="https://www.shodan.io/search?query=" + query

r = requests.get(url)
print(r.status_code)

data = bb(r.text, "html.parser")

d1 = data.find_all("div", class_="heading")

for i in d1:
    d2 = i.find("a", class_="title text-dark")
    print(d2.string)




