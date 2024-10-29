import math
from bisect import insort
from itertools import count
from operator import index, truth

#
# my_list = [3,4,2,1,1,2]
# print(my_list)
#
# empty_list = []
# print(empty_list)
# mixed_list = [1,"hello", 3.18,True]
# print(mixed_list)
#
# #Accessing Element
# print(my_list)
# first_element=my_list[0]
# last_element=my_list[-1]
# print(first_element)
# print(last_element)
#
# #adding element
#
# my_list.append(6)
# print(my_list)
# my_list.insert(1,15)
# print(my_list)
# my_list.extend(["string",9,True])
# print(my_list)
#
# #Removing element
#
# del my_list[0]
# print(my_list)
#
# removed_element=my_list.pop(1)
# print(removed_element)
# print(my_list)
# my_list.remove(9)
# print(my_list)
#
# #finding index of element
#
# print("finding index of element")
# print(my_list)
# # index_of_seven=my_list.index(7)
# # print(index_of_seven)
#
# #find number of occurance
#
# occurance_count=my_list.count(4)
# print(occurance_count)
#
# #sorting the list
# print("sorting")
# my_list=[3,4,5,6,7]
# my_list.sort()
# print(my_list)
#
# #reversing
# print("reversing")
# my_list.reverse()
# print(my_list)
#
# #copying a list
#
# my_list_copy =my_list.copy()
# print(my_list_copy)
#
#
# another_copy=my_list[:]
# print(another_copy)
#
# #clearing a list
#
# my_list.clear()
# print(my_list)
#
# #joining a list
# list1=[1,2,3,4,5]
# list2=[6,7,8,9,10]
#
# combined_list=list1+list2
# print(combined_list)
#
# #slicing
#
# my_list=[1,2,3,4,54,5,6,7,10]
# sub_list=my_list[1:3]
# print(sub_list)
#
# #nested list
#
# nested_list=[[1,2],[3,4],[5,6]]
# print(nested_list)
# print(nested_list[0][0])

#Assignment 5 based on List
#
# to_do_list = []
#
# while(True):
#     print("1. Add to List , 2. Remove From List , 3. View List, 4. Exit")
#     op = int(input("Enter the operation number you want "))
#     match op:
#         case 1:
#             a= input("Enter List object ")
#             to_do_list.append(a)
#             print(to_do_list)
#         case 2:
#             a1 = input("Enter List object that want you to remove ")
#             to_do_list.remove(a1)
#         case 3:
#             print(to_do_list)
#         case 4:
#             exit()


#
# #Assignment 6:prime number
# list_prime=[]
#
# prime= int(input("Enter a number"))
#
# for i in range(2,prime):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         list_prime.append(i)
#
# print(list_prime)
#
#
# for i in range(2,prime):
#     for j in range(2,i):
#         if i%j!=0:
#             list_prime.append(i)
#     else:
#         break
#
# print(list_prime)

#
# def is_prime(num):
#     if num<2:
#         return False
#     for i in range(2, int(num**0.5) +1):
#         if num%i==0:
#             return False
#     return True
#
# is_prime(100)
#
# #Assignment 7:
#
y_list = [1, 2, 3, 4, 5]
emp_list = []

print("Original list:", y_list)

# Input: number of positions to rotate
pos = int(input("Enter the number of positions to rotate: "))

# Rotation logic
# Use modulus to handle cases where pos > len(y_list)
pos = pos % len(y_list)

# Rotating the list
emp_list = y_list[-pos:] + y_list[:-pos]

print("Rotated list:", emp_list)


















