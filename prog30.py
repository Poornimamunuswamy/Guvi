from datetime import datetime
s1 = input("")
s2 = input("")
format = '%H:%M'
time = datetime.strptime(s2, format) - datetime.strptime(s1, format)
print(time)
