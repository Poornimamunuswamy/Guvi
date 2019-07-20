a=int(input("Enter a number: "))
if(a>2):
    for i in range (1,1000,1):
        b=a%i
    if(b==0):
        print("no")
    else:
        print("yes")
else:
    print("no")
