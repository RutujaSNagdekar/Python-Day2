# fruit='apple'
#
# match fruit:
#     case "apple":
#         print("you like apple")
#     case "banana":
#         print("you like banana")
#     case "_":
#         print("I dont know what you like")
from colorsys import yiq_to_rgb

#Assignment2 create cal for performing +,-,/,* using match-case


op1=print("1.Addition","2.Substraction","3.Division","4.Multiplication")
num1=int(input("Enter num1:"))
num2=int(input("Enter num2:"))
op=input("Enter your operation:")

match op:
    case "Addition":
        print("Addition:",num1+num2)
    case "Substraction":
        print("Substraction:", num1 -num2)
    case "Division":
        print("Division:", num1 //num2)
    case "Multiplication":
        print("Multiplication:", num1 * num2)
    case "_":
        print("Invalid operation....")
#
# op2= input("Do you want to continue? Y/N:")
# if op2==y:
#     continue
# else:
#     break