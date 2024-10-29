balance=float(input("enter account balance:"))
n=1
while(True):
    withdraw = float(input("Enter amount you wish to withdraw:"))
    if withdraw%10==0:

        if withdraw>balance:
            print("insufficient amount ...")
        else:
            balance = balance - withdraw
            print("balance:",balance)
            print("withdrawal successful...")

        print("You wanna continue?")
        n = int(input("Enter value of n "))
        if n == 1:
            continue
        else:
            break
