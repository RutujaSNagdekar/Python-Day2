#!usr/bin/python3

def data(op):
    if op==1:
        yield 3+4
    #print("hello")
    if op==2:
        yield 4-3
    #yield a*b
    
    #yield a/b




#print(data(2,3).__next__())    # always returns first yield
#print(data(2,3).__next__())    #Again returns first yield


#out = data(2,3)    #Need to store function in var

#Always Sequential OP returned 
#print(next(out))   #Returns OP of first yield

#print(next(out))   #Returns OP of second yield


op=int(input("enter your operation"))
print(data(op))

