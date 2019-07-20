n=int(input("Enter the number "))
temp=n
rev=0
if(n<=1000):
    while(n>0):
        a=n%10
        rev=rev*10+a
        n=n//10
    if(temp==rev):
        print("yes")
    else:
        print("no")
else:
    print("Please enter a number from 1 to 1000")
