num = int(input(""))
a=0
b=1
sum=0
for i in range(0,num):
       c=a+b
       a=b
       b=c
       sum+=1
       print(a)
