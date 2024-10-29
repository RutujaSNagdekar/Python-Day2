#!/usr/bin/python3

import json

with open("data.json","r") as f1:
    jj= json.load(f1)
print(jj["data"]["email"])
print(jj["support"]["url"])
