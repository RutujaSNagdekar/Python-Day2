#!/usr/bin/python3
import requests

url = "https://www.google.com"
res = requests.get(url)
print(res.status_code)
#print(res.text)  #Whole Document text

