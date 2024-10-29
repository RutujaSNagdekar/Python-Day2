#
# #Assignment 5 - Add Integer and float

num1 = int(input("Enter Integer Value"))
num2= float(input("Enter Float Value"))
print("Adding Int and Float", num1+num2)
print(type(num1+num2))


#Assignment 6 - Float Square
num3= float(input("Enter Float Value"))
print("Square of Float is",num3*num3)


#Assignment 7
num4= input("Enter string")
num5 = input("Enter Integer Value")
print("add:",num4+num5)
print(type(num4+num5))

#Assignment 11--Implement all comparsion operator
#==,!=,>=,<=

a=input("enter a:")
b=input("enter b:")

if a==b:
    print("a is equal to b")
elif a!=b:
    print("a is not equal to b")
elif a>=b:
    print("a is greater than b")
elif a<=b:
    print("a is less than b")
else:
    print("invalid")




#Assignmnent 12: Build a calculator for +,-,*,/ operations using if and else condition statement

while(1):
    op = input("Enter operator(+,-,*,/):")

    num1 = int(input("Enter num1:"))
    num2 = int(input("Enter num2:"))

    if op == '+':
        print(num1 + num2)
    elif op == '-':
        print(num1 - num2)
    elif op == '*':
        print(num1 * num2)
    elif op == '/':
        print(num1 / num2)
    else:
        print("invalid operator")

    cn=input("Enter your choice y/n ")
    if(cn=='y'):
        continue
    else:
        break


#Assignment 13

while(1):

    age = int(input("Enter your age"))

    if age <= 5:
        print("Free")
    elif age >= 5 and age <= 12:
        print("Rs 5")
    elif age >= 13 and age <= 60:
        print("Rs 10")
    else:
        print("Rs 7")

    cn = input("Want to continue? y/n ")
    if cn=='y':
        continue
    else:
        break





