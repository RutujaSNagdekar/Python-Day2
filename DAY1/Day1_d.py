#if else statement

num=12
if num%2==0:
    print("the number is even")
else:
    print("the number is odd")

#comparing
inum1=1
inum2=1

if inum1 != inum2:
    print("NUM1 is Not equal to NUM2")
else:
    print("Num1 is equaL to Num2")


iScore = int(input("Enter your Score"))

if iScore>=90:
    print("Grade A")
elif iScore>=80:
    print("Grade B")
elif iScore>=70:
    print("Grade C")
elif iScore>=60:
    print("Grade D")
else: print("Grade E")