#!/usr/bin/python3


import json, requests, pickle

urls = [
    "https://reqres.in/api/users?page=1",
    "https://reqres.in/api/users?page=2"
    ]

for i in urls:
  data = requests.get(i, timeout=10)
  json_bytes = pickle.dumps(data.text)
  plain_json = pickle.loads(json_bytes)
  print(plain_json)


