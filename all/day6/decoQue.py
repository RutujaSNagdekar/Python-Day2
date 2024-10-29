#!/usr/bin/python3

def d1(func):
    def w1():
        return "<ol>" + func() + "</ol>"
    return w1

def d2(func):
    def w2():
        return "<li>" + func() + "</li>"
    return w2

@d1
@d2
def who():
    item = input("Enter the item you want")
    return item

a = who()
print(a)





