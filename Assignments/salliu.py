ls = input("Enter list")
ls=ls.split(",")
print(ls)
list1 = []
for i in range(1,len(ls)+1):
    for j in range(i):
        #list1 = []
        list1.append(ls[j])
        print(list1)

    print("\n")


