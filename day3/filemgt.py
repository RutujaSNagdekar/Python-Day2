#!/usr/bin/python3

f1 = open("file.txt", "w")
f1.write("this is file1")
f1.close()

f2 = open("file.txt", "r")
a = f2.read()
print(a)
f2.close()


f3 = open("file.txt", "a")
f3.write("hello bro...\n")

f3.close()

with open("file.txt", "r") as f4:
    a = f4.readlines()
    print(a)
