#!/usr/bin/python3
from queJson import r
import json

#data = jj["data"]


dataset = r.text

with open("data_sets.json","w") as f1:
    f1.write(dataset)

with open("data_sets.json","r") as f2:
    jj = json.load(f2)
#print(jj)
print(type(jj))
data = jj["data"]
num =int(input("Enter user id"))


if __name__=="__main__":
    def datafun(idnum):
        #print(jj["data"][idnum-1])

        try:
            for i in range(len(data)):
                if idnum == data[i-1]["id"]:
                    print("First name:",jj["data"][i-1]["first_name"])
                    print("Last name:",jj["data"][i-1]["last_name"])
                    print("Email",jj["data"][i-1]["email"])
                    print("Avatar:",jj["data"][i-1]["avatar"])

        except:
            print("Enter Valid ID")

datafun(num)



