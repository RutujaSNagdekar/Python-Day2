#!/usr/bin/python3

import requests
import json 

url = "https://reqres.in/api/users/"
head = {"User-Agent": "", "Content-type":"application/json"}
r = requests.get(url, headers=head, timeout=10,allow_redirects=True)

#print(r.status_code)
#print(r.text)







