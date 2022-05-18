import matplotlib.pyplot as plt
import matplotlib.colors as color
import numpy as np
import random
data=np.load("杭州mergedXY.npy")
print(data)
demandCoordinates=[(data[i][0],data[i][1]) for i in range(data.shape[0])]
size=data.shape[0]
q=[random.random()*10 for i in range(size)]

A=[(i,j) for i in range(size) for j in range(size)]
N=[i for i in range(size)]
dis={(i,j):np.hypot(demandCoordinates[i][0]-demandCoordinates[j][0],demandCoordinates[i][1]-demandCoordinates[j][1]) for i,j in A}


markersize=3
linewidth=0.5
n=np.load("n.npy")
x=np.load("x.npy")
for i in N:
    xy=demandCoordinates[i]
    if (n[i]>0):
        continue
    plt.plot(xy[0],xy[1],c="b",marker="s",markersize=markersize)
    #plt.text(xy[0],xy[1],f"{q[i]}")

# 画需求量

nMax=0.0
for ni in N:
    # print(type(n[ni].x),n[ni].x,type(nMax))
    if n[ni]>nMax:
        nMax=n[ni]

for i in N:
    if (n[i]>0):
        xy=demandCoordinates[i]
        col=plt.cm.rainbow
        norm=color.Normalize(vmax=round(nMax)+1,vmin=0)
        # plt.plot(xy[0],xy[1],marker="s",color='g',markersize=markersize)
        plt.plot(xy[0],xy[1],marker="s",color=col(norm(n[i])),markersize=markersize)
        # plt.text(xy[0]-5,xy[1]-5,f"{n[i].x}",color="b")
        

# 画供应线
for i,j in A:
    if x[i,j]>0.0:
        demandCoordinates[i][0],demandCoordinates[i][1]
        demandCoordinates[j][0],demandCoordinates[j][1]
        plt.plot([demandCoordinates[i][0],demandCoordinates[j][0]],[demandCoordinates[i][1],demandCoordinates[j][1]],color="r",linewidth=linewidth)



plt.xlabel("x")
plt.ylabel("y")
plt.show()

    