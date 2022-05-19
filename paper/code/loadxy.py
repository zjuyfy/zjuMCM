import numpy as np
with open ("杭州xy.txt",mode="r") as f:
    str = f.readlines()
size=int((str[-1].split(',')[0]))+1
data = np.zeros((size,2), dtype = float)
a=str[1].split(",")
for line in str[1:]:
    list=line.split(',')
    data[int(list[0])][0]=list[1].strip("\n")
    data[int(list[0])][1]=list[2].strip("\n")
np.save("杭州xy",data)
demandCoordinates=[(data[i][0],data[i][1]) \
    for i in range(data.shape[0])]
print(data)
#np.save("xy坐标",data)