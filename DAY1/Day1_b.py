
#typecasting
str = "1"
print(str)
print(type(str))

intstr = int(str)
print(intstr)
print(type(intstr))

#Assignment 3- Arithmatic operator and Assignment Operator

print("Result:",2+4)
print("result type:",type(2+4))

print("Result:",2-4)
print("result type:",type(2-4))

print("Result:",2*4)
print("result type:",type(2*4))

print("Result:",2/4)
print("result type:",type(2/4))

print("Result:",6//4)
print("result type:",type(6//4))

print("Result:",2%4)
print("result type:",type(2%4))

print("Result:",2**4)
print("result type:",type(2**4))

##Assignment operator(=)

x=10
print("Assignment operator:",x)

x+=10
print(" Augmented assignment operator(+=)",x)

x-=10
print(" Augmented assignment operator(-=)",x)

x*=10
print(" Augmented assignment operator(*=)",x)

x/=10
print(" Augmented assignment operator(/=)",x)

x%=10
print(" Augmented assignment operator(%=)",x)

x=10
x**=6
print(" Augmented assignment operator(**=)",x)

x//=10
print(" Augmented assignment operator(//=)",x)


a=20
b=7
print(a**b)
print(a//b)

#Console interactions
#Assignment 5 - accept 2 number from user add them and print them`
inum1 = int(input("Enter first number "))
inum2 = int(input("Enter second number "))
print("Your numbers are", inum1+ inum2)

#Format to 2 decimal places
x=2.3434343423

print(f"Number Value:{x:.2f}")


#Accpet 2 strings from user and print them
#using formate function
firstname=input("enter first name:")
lastname=input("enter your last name:")

print(firstname+lastname)
print(firstname,lastname)

print('hi my first name is:{} my last name is :{}'.format(firstname,lastname))

print('hi my name is :{lname} I am {fname} years old'.format(fname=firstname,lname=lastname))

#using 'sep' keyword
print("Hello","world",sep=' ')
print("Hello","world",sep='_')
print("Hello","world",sep=', ')

#using 'end' keyword
print("hello,world",end=' ')
print("This is after end")

