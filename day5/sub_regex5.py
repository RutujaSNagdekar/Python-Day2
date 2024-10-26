#!/usr/bin/python3

import re

with open ("datanumbersregex","r") as f:
    dd=f.readlines()
    for i in dd:
        collect=re.sub("^[\d]{10}", "+91"+ i, i.strip("\n"))
        if collect:
            print(collect.strip("\n"))


print(type(collect))

