import pandas as pd
x=[3,2,35,5,3,5,66.4,43.5,2344,45,33,4,543,334,322] # Due to 2 float values datatype changed to float

a = pd.Series(x)
print(type(a))
print(a)  #### To print the entire 1D array
print(a[2])  #### To print the data of 2nd index value from 1D array
print()

print("Dict to Dataframe")
d = {"name":["mohit","rohit","nandan","tanishq"],"rank":[1,2,3,4],"role":["dev","devops","tester","hacker"]}
d1 = pd.Series(d)
print(d1)   #Returns type object as multiple datatype available




