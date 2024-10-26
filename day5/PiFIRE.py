#!/usr/bin/python3
import pickle,re,requests


url="https://pastebin.com/raw/AnyRPQJV"
data=requests.get(url)
print(data.status_code)


#Using Pickle dump and load
with open('dump1.pkl','wb') as f:
    a= pickle.dump(data.text,f)
    print(a)

with open('dump1.pkl','rb') as f:
    loaded_data=pickle.load(f)
    #print(loaded_data)
#print(type(loaded_data))
cnt =0


r = re.findall("pizza", loaded_data)
for i in r :
    cnt+=1
    print(i)
print("*************Count of Pizza*************", cnt)







