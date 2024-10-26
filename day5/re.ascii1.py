#!/usr/bin/python3
import re

string = "sdhsRegEx%&%%%%&%&^&@!$#$%%^^%"


r = re.finditer("RegEx", string, re.A)
for i in r:
    #print(r)    Prints Address
    print(i.group())
