a=int(input("Enter the number of elements: "))
b=int(input("Enter the range: "))
print("Enter the elements one by one: ")
arr=[]
sum=0
for i in range (a):
    n=int(input(''))
    arr.append(n)
for i in range (b):
    sum=sum+arr[i]
print(sum)
    
