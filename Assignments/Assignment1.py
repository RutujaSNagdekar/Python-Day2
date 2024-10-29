"""
Question 1
Write a program to find the factors of a given number and check whether the factor is even or odd.

# """


num = int(input("Enter a Number"))

for i in range(1,num+1):
    if num%i==0:
        print("Factor is",i)
        if i%2==0:
            print("Factor is Even")
        else:
            print("Factor is Odd")


"""
Question 2
Write a code that accepts a sequence of words as input and prints the words in a sequence after sorting them alphabetically.

"""

str = input("Enter String")
print(str)
l1 = str.split()
l1.sort()
print(l1)

"""
Question 3
Write a program that will find all the numbers between 1000 and 3000 
(both excluded) such that each digit of a number is an odd number. 
Print the number of such elements
# 
# """
def oddnum(num):
    for digit in str(num):
        if int(digit)%2==0:
            return False
    return True

oddlist = []
for i in range(1001,3000):
    if oddnum(i):
        oddlist.append(i)

print(oddlist)
print("Count of Odd-Digit Numbers", len(oddlist))


"""
Question 4. 
Write a program that accepts a string and calculates the number of letters and digits.
 Suppose if the entered string is: qwerty123 Then the output will be: LETTERS: - 6 DIGITS: - 3
"""
str = input("Enter String")
cnt1=0
cnt2=0

for char in str:
    if char.isalpha():
        cnt1+=1
    elif char.isdigit():
        cnt2+=1

print("LETTERS: ",cnt1 , "DIGITS: ", cnt2)


"""
Question5 
Design a code which will find whether the given number is Palindrome number or not
"""

num = input("Enter Number")

if num==num[::-1]:
    print("NUmber is Palindorme")
else:
    print("Number is not Palindrome")









