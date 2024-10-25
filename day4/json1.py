#!/usr/bin/python3
import json
data = '{"data": {"id": 1,"email": "janet.weaver@reqres.in","first_name": "Janet","last_name": "Weaver","avatar": "https://reqres.in/img/faces/2-image.jpg"},"support": { "url": "https://reqres.in/#support-heading", "text": "To keep ReqRes free, contributions towards server costs are appreciated!"}}'

jj = json.loads(data)
print(jj)
print(type(jj))
print(jj["data"]["email"])


## OUT: janet.weaver@reqres.in

