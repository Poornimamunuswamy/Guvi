n=int(input("Enter the number: "))
temp=n
sum=0
while n>0:
    a=n%10
    sum=sum+a**3
    n=n//10
if(temp==sum):
    print("yes")
else:
    print("no")
