#!/usr/bin/python3
import time
def decorator(func):
	def wrapper():
		print("Starting function...")
		func()
		print("Function ends...")
	return wrapper




@decorator
def fun():
	print("you merely adopted the dark i was born in it")
	time.sleep(2)

fun()



