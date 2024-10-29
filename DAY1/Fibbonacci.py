from DAY1.Day1_b import firstname

n = int(input("Enter number"))

n1 =0
n2=1
print(n1, end=' ')
print(n2, end=' ')
sum1 = n1+n2
print(sum1, end= ' ')

for i in range(2, n):
    for j in range(n+1,100):
        sum1= sum1+i
        print(sum1, end=' ')

first=0
second=1

first,second=first,second+1
#for i in range(2,i+1):




