
#!/usr/bin/python3
import requests

url = "https://miro.medium.com/v2/resize:fit:1100/format:webp/1*_Wde2bdsU1BGZBhEjWKaVw.png"
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
data = requests.get(url, headers=header, timeout=5, allow_redirects=True)

#print(data.text)

with open("file.png", "wb") as html:
    html.write(data.content)


