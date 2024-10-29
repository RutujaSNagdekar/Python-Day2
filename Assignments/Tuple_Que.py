# sample = (1,2,3,4,3,2,4,6,7,8,6,4,3,2)
# s  = set(sample)
# print(s)
#
# for i in s :
#     print("Count of " , i ,sample.count(i))
from itertools import count
from random import sample

#Question2

sample_list = [10,20,30,(40,50),60]
print(sample_list)
count=0
for i in sample_list:
    if type(i)==tuple:
        break
    count+=1
    print(i)
print("output:",count)

