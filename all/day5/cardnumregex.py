#!/usr/bin/python3
import requests
import re

url = "https://www.bincodes.com/random-creditcard-generator/"

data = requests.get(url)
#print(data.status_code)
numdata = data.text

num = re.findall(r"\d{14,16}", numdata)
for i in num:
    print(i)
    








