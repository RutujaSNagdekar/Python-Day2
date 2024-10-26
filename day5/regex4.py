#!/usr/bin/pyhton3

import re

with open("dataregex","r") as f:
    dd=f.read()
    collect=re.sub("com","cdac.in",dd)
    if collect:
        print(type(collect))
        print(collect)
