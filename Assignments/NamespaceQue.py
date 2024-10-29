sum =0   #global variable
print("Initial Sum",sum)  #Initial sum value

def fun1():

    sum1=0   # Local varialbe
    num = input("Enter List of Numbers")
    num=num.split()
    for i in num:
        sum1+=int(i)
    return sum1

sum = fun1()
print("Returned Sum value",sum)  #Updated sum value




