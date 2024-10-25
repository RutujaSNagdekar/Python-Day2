#!/usr/bin/python3
import pickle

data=[1,2,3,4,5]

with open('bytes_stream.pkl','wb') as f:
    a= pickle.dump(data,f)
    print(a)

with open('bytes_stream.pkl','rb') as f:
    loaded_data=pickle.load(f)
    print(loaded_data)
