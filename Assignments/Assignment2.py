"""
Question1
Check password correct or not
"""
from itertools import count

li = ['@', '&']

password = input("Enter your Password")

alpha=False
digit=False
char=False


if len(password)>=5 and len(password)<=10:
    for i in password:
        if i.isalpha():
            alpha=True

        elif i.isdigit():
            digit=True

        elif i in li:
            char=True

    if alpha and digit and char:
        print("Password is Valid")
    else:
        print("Password should contain at least one letter, one digit, and one special character")
else:
    print("Password length should be between 5 and 10")


"""
Question 2:
Print all elemnets in list with their indexes
"""

lst = input("Enter List elements")
lst = lst.split()
for i in range(len(lst)):
    print(f"{i}th Element:{lst[i]}")

"""
Output:

Enter List elementsrutuja sakshi pranav
0th Element:rutuja
1th Element:sakshi
2th Element:pranav

"""




"""
Question3
Write a Program which accepts a string from the console and print the characters that 
have even indexes if the Character is an alphabet. Concatenate the characters and print.

"""

str = input("Enter String")
l1=[]
for i in range(len(str)):
    if i%2==0 and str[i].isalpha():
        l1.append(str[i])

print("Concatenated", "".join(l1))

"""
Question4
Write a program which accepts a string from console and print it in reverse order.

"""

str = input("Enter String")
str = str[::-1]
print(str)


"""
Question5
Please write a program which counts and 
prints the numbers of each character in string input by the console.

"""

str = input("Enter String")

s = set(str)
for i in s:
    c= str.count(i)
    print(f"Count of {i}th" , c)




