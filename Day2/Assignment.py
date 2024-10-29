#Assignment1
pattern=int(input("Enter the  number of rows for the pattern:"))


for i in range(1,pattern+1):
    for j in range(1,i+1):
        print(i, end=' ')
    print()

