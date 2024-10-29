#!/usr/bin/python3


import requests
from bs4 import BeautifulSoup as bb

url = "https://realpython.github.io/fake-jobs/"

r = requests.get(url)

data = bb(r.text, "html.parser")

d1 = data.find("div", class_="media-content")
dd =d1.find_all("h2", class_="title is-5")

for i in dd:
    print(i.string)




