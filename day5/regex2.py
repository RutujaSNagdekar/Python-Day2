#!/usr/bin/python3
import requests
import re

cnt=0
with open("dataregex","r")as f:
    dd = f.readlines()
    for i in dd:
        collect = re.search(".*[? &]url=.*" , i.strip("\n")) 
        if collect:
            cnt+=1
            print(collect.group())

print(cnt)
