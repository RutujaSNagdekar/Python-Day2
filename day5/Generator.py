#!usr/bin/python3

def data(a,b):
    yield a+b
    print("hello")
    yield a*b



print(data(2,3).__next__())    # always returns first yield
print(data(2,3).__next__())    #Again returns first yield


out = data(2,3)    #Need to store function in var

#Always Sequential OP returned 
print(next(out))   #Returns OP of first yield

print(next(out))   #Returns OP of second yield


