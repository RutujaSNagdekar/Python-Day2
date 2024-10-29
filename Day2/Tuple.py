# #create a tuple
# #from Day2.List import my_list
#
# tuple_int=(1,2,3,4)
# tuple_str=("a","b","c")
# my_tuple=(1,3.4,"a",True)
# empty_tuple=()
#
# single_element=(5,)
# print(tuple_int)
# print(single_element)
# print(tuple_str)
# print(empty_tuple)
# print(my_tuple)
# print(my_tuple[0],my_tuple[-1])
#
#
# #tuple unpacking
# my_tuple=(10,20,30)
# item1,item2,item3=my_tuple
# print(item1)
# print(item2)
# print(item3)
#
# #concatenation
#
# tuple1=(1,2,3)
# tuple2=(4,5,6)
# combine_tuple=tuple1+tuple2
#
# print(combine_tuple)
#
# #finding length
# my_t=(1,2,3,4,5,6)
# print(len(my_t))
#
# #checking membership
#
# my_t=(1,2,3)
# is_present =2 in my_t
# print(is_present)
# is_present1=5 in my_t
# print(is_present1)
#
# #
# #counting occurence
#
# my_t1=(1,2,3,4,5,3,2,4,6,4)
# print(my_t1.count(4))
#
# #finding index
#
# my_t3=(1,2,3,4,5)
# index_of_3=my_t3.index(3)
# print(index_of_3)
# #Repetition
#
# mytup1= (1,2,3)
# repeated_tup= mytup1*3
# print(repeated_tup)
# print(mytup1)
#
#
# #Sorting a tuple
# mytup2= (2,5,1,4,78,6,4)
# mylist = sorted(mytup2)
# print(mylist)
#
# #Converting list to tuple and vice versa
#
# mytuple1 = tuple(mylist)
# print(mytuple1)
#
#
# #Converting tuple to list and vice versa
#
# my_new_list = list(mytuple1)
# print(my_new_list)
#
# #Sliciing
# mytuple2= (2,4,5,6,7,1,2,3)
# slice_tup = mytuple2[1:-1]
# print(slice_tup)
#
# slice_tup1 = mytuple2[::2]
# print(slice_tup1)
#
# slice_tup3 = mytuple2[::-1]
# print(slice_tup3)
#
# #Nested Tuples
# nested_tuple = ((1,2), (3,4),(5,6))
# first_tuple = nested_tuple[0]
# print(first_tuple)
from operator import index
from os.path import split

#Immutability
# mytuppp= (2,3,4,5)
# mytuppp[0] = 10

#
# #ASSIGNMENT 8
#
# list=["abc","xyz","pqr","lmn"]
# #
# # t=tuple(list)
# # # print(t)
#
# print(list,sep=",")
# tuple1=()
# tuple1=tuple(list)
# print(tuple1)
# first=(tuple1[0])
# print(first)
# last=(tuple1[-1])
# print(last)
# ex=(tuple1[1:-1])
# print(ex)
#
# slice_tup=(tuple1[1::2])
# print(slice_tup)
#
# rev=(tuple1[::-1])
# print(rev)

#Assignment 9
# list1=[]
#
# n = int(input("How many 🤔"))
# for i in range(1,n+1):
#     a= int(input("Enter the integer"))
#     list1.append(a)
# print(list1)
#
# tup = tuple(list1)
# print(tup)
#
# sum = 0
# #Calculate sum
# for i in range(len(tup)):
#     sum+=tup[i]
# print("Sum of tuple is ",sum)
#
# #average of tuple
# # avg = sum/ len(tup)
# # print("Average of tuple is",avg)
# #
# # #Maximun and Minimun values
# # sorted_tup = sorted(tup)
# # max = sorted_tup[-1]
# # min = sorted_tup[0]
# # print("Max of tuple is", max)
# # print("Min of tuple is", min)
# #
# # #NUmber of elements in tuple
# # no= len(tup)
# # print("Length of tuple is", no)
#
#
# # #Assignment 10
# # name=input("enter names:")
# # age=int(input("enter age:"))
# # city=input("enter city")
# # country=input("enter country:")
# # nested_tuple= (city, country)
# # tuple_1=(name,age,nested_tuple)
# # #name,age= tuple_1
# # print(tuple_1)
# #
# #
# # n,a,(c1,c2) = tuple_1
# # print(n,a,c1,c2)
#
#
# SSIGNMENT 11
#
# liststd= []
#
# for i in range(1,3):
#     name = input("Enter your name:")
#     roll_no = int(input("enter your roll number:"))
#     percentage = int(input("enter your percentage:"))
#     liststd.append((name,roll_no,percentage))
#
# #Display details of studnets
# for i in range(len(liststd)):
#     print(f"Student in the list are{i}:{liststd[i]}")
#
# threshold = 60
# for i in range(len(liststd)):
#     if liststd[i][2]>threshold:
#         print(f" Names of the Students above threshold are :{liststd[i][0]}")
#
# rollno= int(input("Enter the Roll number of student u wanted"))
#
# for i in range(len(liststd)):
#     if rollno == liststd[i][1]:
#         print(liststd[i])
# avgstd=0
# for i in range(len(liststd)):
#     sumstd=0
#     sumstd += liststd[i][2]
#     avgstd = sumstd/len(liststd)
# print(avgstd)
#
# #A
# mylis=  [2,3,4]
# mylis.append([4,5])
# print(mylis)

m=(1,2,3)*2
print(len(m))

















