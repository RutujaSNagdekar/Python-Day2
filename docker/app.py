#!/usr/bin/python3

import requests
url = "http://testphp.vulnweb.com"
d = requests.get(url)
print(d.text)
