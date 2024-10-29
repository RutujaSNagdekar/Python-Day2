#!/usr/bin/python3
import requests 

url = "https://webhook.site/0231cba9-8c68-40f1-8c65-379317c30912"
head = {"User-Agent": "me-rutuja"}

res = requests.get(url, headers = head)
print(res.status_code)




