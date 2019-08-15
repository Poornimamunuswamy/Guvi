import statistics
n=int(input(""))
ar=[]
for i in range(n):
    c=int(input(""))
    ar.append(c)
print(statistics.median(ar))
