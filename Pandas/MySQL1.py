from idlelib.editor import keynames
from re import match
import pickle
import os
import mysql.connector


#connect = mysql.connector.connect(host="localhost", user="root", password="root", database="classicmodels")
connect = mysql.connector.connect(host="localhost", user="root", password="root", database="classicmodels")
print(connect)
a = connect.cursor()  #Connect to console


def db():   #1
    a.execute("show databases;")
    db = a.fetchall()
    print(db)
    print("*************************************")

def tb():   #2
    a.execute("show tables;")
    db = a.fetchall()
    return len(db)
    print("*************************************")

def listTb():  #3
    a.execute("show tables;")
    db = a.fetchall()
    #Using Pickle Load and dump
    with open("data.pkl", "wb") as file:
        pickle.dump(db,file)
    with open("data.pkl","rb") as file1:
        data = pickle.load(file1)
    print(data)
    print("*************************************")

def tbwithoutData(): #4
    with open("data.pkl", "rb") as file1:
        data = pickle.load(file1)
    print(data)
    ip = input("Enter the table you want")
    a.execute("desc " + ip)
    db = a.fetchall()
    print(db)
    print("*************************************")

def tbwithData():  #5
    with open("data.pkl", "rb") as file1:
        data = pickle.load(file1)
    print(data)
    data1={}
    ip = input("Enter the table you want")
    key=ip
    a.execute("select * from "+ ip)
    db = a.fetchall()
    data1[key] = db
    print("Printing Data from "+ ip)
    print(data1)
    print("*************************************")

def data() -> None:
	a.execute("show tables")
	result = a.fetchall()
	with open("tables.pkl", "wb") as f:
		pickle.dump(result, f)


def table() -> list:
	if not os.path.exists("tables.pkl"):
		data()
	with open("tables.pkl","rb") as f:
		result = pickle.load(f)
	return result

def raw_data():
	result = table()
	dic = {}
	for i in result:
		a.execute(f"Select * from {i[0]}")
		r = a.fetchall()
		dic.update({i[0]: r})
	with open("raw_data.pkl", "wb") as f:
		pickle.dump(result, f)
	return dic

def tbwithAllData():  #6
    dic = raw_data()
    print(dic)


    print("*************************************")



while(1):
    print("Interacting with DB_version" )
    print("1. Show DB Name")
    print("2. Table Name")
    print("3. List Table")
    print("4. Columns name from table")
    print("5. All columns from table")
    print("6. All data from All tables")
    op = int(input("Enter Operation u want: "))

    match op:
        case 1:
            db()
        case 2:
            print(tb())  # Returns length of db tables
        case 3:
            listTb()
        case 4:
            tbwithoutData()
        case 5:
            tbwithData()
        case 6:
            tbwithAllData()









