import mysql.connector

#connect = mysql.connector.connect(host="localhost", user="root", password="root", database="college")
connect = mysql.connector.connect(host="localhost", user="root", password="root", database="college")
print(connect)

a = connect.cursor()
print(a.execute("desc emp"))    #Prints None

result = a.fetchall()   #fetchone
for i in result:
	print(i)


