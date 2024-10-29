#!/usr/bin/python3
import time
def decorator1(func):
    def wrapper():
        print("Starting 1st wrapper function...")
        func()
        print("Function ends...")
    return wrapper

def decorator2(func):
  def wrapper():
    print("Starting 2nd wrapper function...")
    func()
    print("Function ends...")
  return wrapper

@decorator1
def fun1():
    print("Part1:you merely adopted the dark i was born in it")
    time.sleep(2)

@decorator2
def fun2():
    print("Part2:you merely adopted the dark i was born in it")
    time.sleep(2)

@decorator1
@decorator2
def fun3():
    print("Part3:you merely adopted the dark i was born in it")
    time.sleep(2)


fun1()
fun2()
fun3()



