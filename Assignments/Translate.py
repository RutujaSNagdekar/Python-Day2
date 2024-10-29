input_str="this is fun"
print(input_str)
l= ['a','e','i','o','u']

str = ""

for i in input_str:
    if i not in l  and i.isalpha():
        str += i + "o" + i
    else:
        str += i
print(str)
