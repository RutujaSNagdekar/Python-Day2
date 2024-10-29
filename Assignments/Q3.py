N = input("Enter how many students you want")

l1=[]
for i in range(int(N)):
    studentid= int(input("enter your id:"))
    sname= input("enter your name:")
    marks = input("Enter marks")
    marks = marks.split()

    d= {"SID":studentid,"Sname": sname,"Marks":marks}
    l1.append(d)
    print(d)

print(l1)

#Seach by ID
id = int(input("Enter ID"))
for i in range(len(l1)):
    if l1[i]["SID"] ==id:
        print(l1[i])

#Search by Name
st = input("Enter Name")
for i in range(len(l1)):
    if l1[i]["Sname"] == st:
        print(l1[i])



