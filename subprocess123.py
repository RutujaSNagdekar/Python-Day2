#!/usr/bin/python3
import subprocess as ss
import os

s=ss.getoutput("pwd")
print("With SubProcess-Getoutput:" , s)
s1 = os.system("pwd")
print("With OS-System", s1)

process = ss.Popen(["pwd"], stdout = ss.PIPE, stderr = ss.PIPE) 
a,b = process.communicate();
print("Process a", a)
print("Process b",b)
print("Process Object", process)
