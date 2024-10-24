#!/usr/bin/python3
def fun1(*args):
    print(type(args))
    print(args)
     print(args[0])
    print(args[2])
fun1(1,2,3,4,5,6,7) 


def test(**kwargs):
    print(kwargs)
    for keys, values in kwargs.items():
        print(keys)
        print(values)

test(a="LOL", b="KIDS")
