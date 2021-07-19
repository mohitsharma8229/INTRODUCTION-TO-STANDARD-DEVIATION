import csv
from collections import Counter 
from os import read
with open('SOCR-HeightWeight.csv',newline='')as f:
    reader=csv.reader(f)
    file_data=list(reader)

file_data.pop(0)
new_data=[]
for i in range(len(file_data)):
    n_num=file_data[i][1]
    new_data.append(float(n_num))

n=len(new_data)
total=0
for x in new_data:
    total=total+x

mean=total/n
print("mean is"+str(mean))

new_data.sort()

if n%2==0:
    m1=float(new_data[n//2])
    m2=float(new_data[n//2-1])
    median=(m1+m2)/2

else:
    median=new_data[n//2]

print("median is "+str(median))

data=Counter(new_data)
mode_data={
    "50-60":0,
    "60-70":0,
    "70-80":0
}
for height,occur in data.items():
    if 50<float(height)<60:
        mode_data["50-60"]+=occur
        
    elif 60<float(height)<70:
        mode_data["60-70"]+=occur

    elif 70<float(height)<80:
        mode_data["70-80"]+=occur

    
mode_range,mode_occur=0,0
for range,occur in mode_data.items():
    if occur>mode_occur:
        mode_range,mode_occur=[int(range.split("-")[0]),int(range.split("-")[1])],occur

    
mode=float((mode_range[0]+mode_range[1])/2)
print(f"mode is {mode:2f}")