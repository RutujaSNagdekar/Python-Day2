#!/usr/bin/python3

import sys
import re

def validate(str1):
    str2 = re.findall("[A-Za-z]{8,20}" , str1)
    print(str2)
    if len(str2) >= 8:
        print(True)
    else:
        print(False)

if __name__=="__main__":
    validate(sys.argv[1])





