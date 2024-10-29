
#!/usr/bin/python3
import pandas as pp

print(pp.__version__)

data = {
	"key1" : ['value1','value2','value3','value4','value5','value6','value7'],
	"key2" : [1111, 2222, 3333, 4444, 5555, 6666, 7777],
	"key3" : [2000, 3000, 4000, 5000, 6000, 7000, 8000]
}

print(type(data))
dd = pp.DataFrame(data)
print(type(dd))
print(dd)
dd
print()

x = pp.DataFrame(data, columns=["key2","key3"])
print(x)
x.insert(1,"Concat_Column",x["key2"].astype(str) + x["key3"].astype(str))
print(x)
print()

x1 = pp.DataFrame(data)
print(x1["key1"][3])
print()

list_1 = [[1,2,3,4,5],[6,7,8,9,10]]
x2 = pp.DataFrame(list_1)
print(x2)

