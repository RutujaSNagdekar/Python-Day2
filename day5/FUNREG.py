#!/usr/bin/python3
import re

def correct(str1):
    newstr = re.sub("[ ]{2,}", " ",str1) 
    newp = re.sub ("\.",". ",newstr)
    print(newp, end="")


if __name__=="__main__":
    str1 = input("Enter a String")
    correct(str1)
