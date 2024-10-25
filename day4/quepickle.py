#!/usr/bin/python3
from queJson import r
import json, requests,pickle


json_bytes = pickle.dumps(r.text)
plain_json = pickle.loads(json_bytes)
#print(plain_json)


jj = json.loads(plain_json)

data = jj["data"]
num =int(input("Enter user id : "))


if __name__=="__main__":
    def datafun(idnum):
        try:
            Found = False
            for i in range(len(data)):
                if idnum == data[i-1]["id"]:
                    print("First name:",jj["data"][i-1]["first_name"])
                    print("Last name:",jj["data"][i-1]["last_name"])
                    print("Email",jj["data"][i-1]["email"])
                    print("Avatar:",jj["data"][i-1]["avatar"])
                    Found = True
                    break
            if not Found:
                raise ValueError ("User id is not valid")
        except ValueError as e:
            print(e)
        
        string = input("Enter all if u want to print all records :")

        if string=="all":
            for i in range(len(data)):
                print("ID:",jj["data"][i-1]["id"])
                print("First name:",jj["data"][i-1]["first_name"])
                print("Last name:",jj["data"][i-1]["last_name"])
                print("Email",jj["data"][i-1]["email"])
                print("Avatar:",jj["data"][i-1]["avatar"])
    


    datafun(num)


