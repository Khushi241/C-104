import csv 
from collections import Counter
with open("data.csv",newline="") as f:
    reader=csv.reader(f)
    file_data=list(reader) 



file_data.pop(0)
new_data=[]
for i in range(len(file_data)):
    n_num=file_data[i][1]
    new_data.append(float(n_num)) 

n=len(new_data)
print(n)
total=0
for x in new_data:
    total += x

print(total)
mean=total/n
print(mean)
new_data.sort()
data=Counter(new_data)
print(data)
#print(new_data)
if n%2==0:
    median1=float(new_data[n//2])
    median2=float(new_data[n//2-1])
    median=(median1+median2)/2
else:
    median=new_data[n//2]

print(median)