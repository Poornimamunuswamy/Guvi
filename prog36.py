s=input("")
count=0
for i in s:
    if((i.isnumeric()==0)& (i.isalpha()==0)&(i.isdigit()==0)):
        count+=1
print(count)
