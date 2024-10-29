import numpy as np
import pandas as pp

d = {'name': ['a','b','c','d','e','f','g','h','i','j'],
     'age': [23,12,55,61,76,89,12,9,27,60],
     "rank":[10,8,6,4,2,1,3,5,7,90]
    }


df1=pp.DataFrame(d,columns=('name','age'))

a=df1.sort_values('age',ascending=False)
print(a.to_numpy())

