import numpy as np
with open ("杭州ODN.txt",mode="r") as f:
    str = f.readlines()
size=int((str[-1].split(',')[2]))-1
print(size)
data = np.zeros((size,size), dtype = float)
for line in str[1:]:
    list=line.split(',')
    data[int(list[2])-2][int(list[3])-1]=list[5].strip("\n")
np.save("杭州ODN",data)
