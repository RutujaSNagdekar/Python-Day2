#!/usr/bin/python3

import re

with open("dataregex","r") as f:
    dd=f.read() 
    collect=re.findall("com",dd)   # no need to use for loop because findall returns list for every non matching
    if collect:
        print(type(collect))
        print(collect) # return list

