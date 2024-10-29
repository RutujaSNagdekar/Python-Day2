#!/usr/bin/python3
import sys,re

for i in sys.stdin.readlines():
    collect = re.sub("ftp","pop",i)
    print(collect)

