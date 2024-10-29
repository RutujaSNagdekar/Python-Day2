#!/usr/bin/python3

import sys
import re

def validate(str1):
    str2 = re.search("[a-zA-Z]{8,20}" , str1)

    if str2:
        print(str2.group())
        print(True)
    else:
        print(False)

if __name__=="__main__":
    validate(sys.argv[1])





