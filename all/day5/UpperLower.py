#!usr/bin/python3
import re

def validate(str1):
    reg1= re.findall("[A-Z]" , str1)
    upper = len(reg1)

    reg2= re.findall("[a-z]" , str1)
    lower = len(reg2)

    return upper, lower


st = input("Enter String: ")
i,j = validate(st)
print(i)
print(j)

