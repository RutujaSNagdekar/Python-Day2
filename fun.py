

def myFunc():
	print("LOL")

# call the function
myFunc()

def add(a, b, c=12):
    x = a + b + c
    return x

x = add(3, 4 )
print(x)

def myFunc() -> bool:
    print(1)
    return True

print(myFunc())


def add2(a: int ,b:int) -> int:
    s =a+b
    return s


print(add2(3,4))


def test(a=12):
    print(a)

test()

def test(a: int, b=12):
    print(a+b)

test(1)

def test(a: int, b: int, c: int, d=12):
    print(a+b+c+d)

test(1,1,1)
