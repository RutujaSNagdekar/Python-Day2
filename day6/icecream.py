#!/usr/bin/python3

def price(func):
    def w3(c,ice):
        print("*****************************")
        a,b = func(c,ice)
        print(f"Your Falvour: {a}")
        print(f"Total Bill:{b} ")


def Chocolate(func):
   # ch = input("You want Chocolate Y/N")
    def w1(c,price):
        ch = input("You want Chocolate Y/N")
        flavour,price= func(c,price)
        if ch=="Y":
            chocolate=80
            chocolate+=price
            return f"You added Chocolate with your icecream with flavour{flavour} ",price 
        else:
            return flavour,price
    return w1

def Sprinkle(func):

    def w2(c,ice):
        ch = input("You want Sprinkle Y/N")
        flavour, price= func(c,ice)
        if ch=="Y":
            sprinkle=50
            price+=sprinkle
            return f"You added Sprinkle with your icecream with {flavour}",price
        else:
            return flavour,price
    return w2


c = input("Enter your icecream falvour: ")
@price
@Chocolate
@Sprinkle
def icecream():
    #c = input("Enter your icecream falvour: ")
    ice = 100
    return c,ice

print(icecream(c,ice))


