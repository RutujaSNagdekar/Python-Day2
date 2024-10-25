#!/usr/bin/python3
import requests


url = "https://unacademy.com/_next/static/~partytown/proxytown"
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36", "Content-Type": "text/plain"}
payload = '{"F":"ohedb9m4jz","M":[0,"tel"]}'
#for i in range(1,10):

data = requests.post(url, headers=header, data=payload,timeout=10, allow_redirects=True)

print(data.status_code)
print(data.text)







