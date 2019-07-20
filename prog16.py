n=int(input("Enter the lower range: "))
q=int(input("Enter the upper range: "))
for num in range(n,q+1):
    if num > 1:
        for i in range(2,num):
            if(num%i)==0:
                break
        else:
            print(num,end=" ")
