# year=int(input("Enter year:"))
#
# if year % 4 ==0 :
#     print("Leap Year")
# elif year % 100 ==0:
#     if year % 400==0:
#         print("It is leap year")
#     else:
#         print("it is not an leap year")
#
# #
# #While Loop
#
# icount = 1
# while icount<=10:
#     print(icount)
#     icount+=1
# else:
#     print("1-10 values printed")
#
# icount = 1
# while(True):
#     print(icount)
#     icount+=1
#
#     if(icount==10):
#         break
#
#
# #Looping in for
# print("For 1-10")
# for i in range(1,10):
#     print(i)
#
# print("For 1-10")
# for i in range(10):
#     print(i)
#
# #Looping on strings
#
# strname = "cdac"
# for strchar in strname:
#     print(strchar)
#
# #nested for loop
# for i in range(3,40):
#     for j in range(1,4):
#         print(f"i={i},j={j}")
#
# #Assignment 15: factorial of a number:using for loop,while loop
# n = int(input("Enter a number: "))
# factorial = 1
#
# if n < 0:
#     print("Factorial is not defined for negative numbers.")
# elif n == 0 or n == 1:
#     print("Factorial of 0 or 1 is 1")
# else:
#     while n > 1:
#         factorial *= n
#         n -= 1
#     print(f"Factorial is {factorial}")
#
# #Assignment 16: wap to calculate the sum of the digit of a  given positive integer
# num1=int(input("Enter positive integer:"))
# sum = 0
# while(num1>0):
#     n = num1 % 10
#     sum+=n
#     num1 = num1 // 10
#
# print(sum)
#
#
#
# #Assignment 17:
#
# num=int(input("Enter positive integer:"))
#
# for i in range(1,11):
#     print(num*i)
#
# #Break and continue
# n=0
# while n<10:
#     n+=1
#     if n%2==0:
#         continue
#     if n == 7:
#             print("number 7 encountered ")
#             break
#
# #print current number
#
#     print(f"current number:{n}")
#

#Assignment 18:Create simple guessing game where the user has to guess a secrete number the game continue until the user guesses
# the correct number this should continue untill the user gets 5 chances

# secnum = 100
# for i in range(1,6):
#     guess = int(input("Guess any number"))
#     if guess==secnum:
#         print("You guess it Correctly****😁😁😁😁😁")
#     else:
#         print("Offoooooooooooooo🤔 Try again... U have {} chances".format(5-i))
#



for i in range(10,0,-1):
    print(i)


#Assignment 19:devlop a program that simulate an ATM withdrwal process
balance = float(input("Enter your account balance:"))

while(True):


    withdraw = float(input("Enter Withdrwal amount:"))

    if balance > withdraw:
        if withdraw%10==0:
            balance=balance-withdraw
            print("Your Remaining Balance :",balance, "Withdrawal is Successful")
        else:
            print("Amount should be Multiple of 10")
    else:
        print("Insufficient balance...")

    print("Wanna Continue? y/n")
    op = input("y/n")
    if(op=='y'):
        continue
    else:
        break


#Assignment 20- wap to evaluate the strength of a user's password based on specific criteria

password = input("Enter Password")








