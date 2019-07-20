n=int(input("Enter the lower range: "))
q=int(input("Enter the upper range: "))
for i in range(n+1,q):
    if(i%2==0):
        print(i,end=" ")
