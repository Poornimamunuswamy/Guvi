n=(input("Enter the number "))
if(n.isnumeric()):
    if(n>0):
        print("Positive")
    elif (n<0):
        print("Negative")
    else:
        print("Zero")
else:
    print("Please enter a number !!!")
