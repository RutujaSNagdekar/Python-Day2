#!/usr/bin/python3
#import sys

#grade = floar

grade=float(input("enter your Score:"))


if grade <= 1 and grade >= 0:
    if grade >=0.9:
        print("Grade A")
    elif grade >=0.8:
        print("Grade B")
    elif grade >=0.7:
        print("Grade C")
    elif grade >=0.6:
        print("Grade D")
    elif grade <0.6:
        print("Grade E")

else:
    print("Value should be between 0 and 1")


