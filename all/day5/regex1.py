#!/usr/bin/python3

import re

with open ("data.txt","r") as f:
    dd=f.readlines()
    for i in dd:
        collect= re.match("http",i.strip("\n"))
        if collect:
            print(collect.group())          #Only collect prints data object
            print(i)

