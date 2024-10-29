#!/usr/bin/python3
from copyreg import pickle
import pandas as pp
import pickle

x = pp.DataFrame({"A":[1,2,3,4],"B":[5,6,7,8],"C":[9,10,11,12]})
print(x)
# To delete column B
x.pop("B")

print(x)

#OR

#del x["A"]
#print(x)


dd = pp.DataFrame(
{
	"key1" : ['value1','value2','value3','value4','value5','value6','value7'],
	"key2" : [1111, 2222, 3333, 4444, 5555, 6666, 7777],
	"key3" : [2000, 3000, 4000, 5000, 6000, 7000, 8000]
}
)

dd.to_csv('dataframes1.csv')  #### also includes index as row

dd.to_csv('dataframes2.csv', index=False)  #### excludes index row
dd1 = pp.read_csv('dataframes1.csv', usecols=["key1"])
print(dd1)	####### To print specific column




with open("raw_data.pkl","rb") as f:
	data = pickle.load(f)

data2 = pp.DataFrame(data)

print(data)
for k, v in data.items():
  d = v['data']
  column = v['column']
  df = pd.DataFrame(d, columns=column)
  df.to_csv(f'{k}.csv', index=False)



