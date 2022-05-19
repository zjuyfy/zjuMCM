import numpy as np
with open ("OD矩阵表.txt",mode="r") as f:
    str = f.readlines()
size=int((str[-1].split(',')[2]))
data = np.zeros((size,size), dtype = float)
a=str[1].split(",")
for line in str[1:]:
    list=line.split(',')
    data[int(list[2])-1][int(list[3])-1]=list[5].strip("\n")
np.save("data",data)