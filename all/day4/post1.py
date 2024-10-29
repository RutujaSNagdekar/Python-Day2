#!/usr/bin/python3
import requests


url = "https://ebooks.adda247.com/api/v1/sms/send?src=aweb"
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36", "Content-Type": "application/json"}
payload = '{"to":"9975369102","messageType":"ADDA"}'
#for i in range(1,10):

data = requests.post(url, headers=header, data=payload,timeout=10, allow_redirects=True)

print(data.status_code)
print(data.text)







