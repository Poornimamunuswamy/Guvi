a=int(input("Enter the lower range: "))
b=int(input("Enter the upper range: "))
for i in range(a,b+1):
    sum=0
    temp=i
    while temp>0:
        c=temp%10
        sum=sum+c**3
        temp=temp//10
    if i==sum:
        print(i,end=" ")

