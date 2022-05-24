
import matplotlib.pyplot as plt
import matplotlib.colors as color
import numpy as np
from gurobipy import Model, GRB , quicksum
# data=np.load("杭州xyn.npy")
data=np.load("杭州mergedXY.npy")

demandCoordinates=[(data[i][0],data[i][1]) \
    for i in range(data.shape[0])]
size=data.shape[0]
A=[(i,j) for i in range(size) for j in range(size)]
N=[i for i in range(size)]
pop_density=np.load("pop_density.npy")
for xy in demandCoordinates:
    plt.plot(xy[0],xy[1],c="b",marker="s")
pop_sum=np.sum(pop_density)
pop_average=pop_sum/size

cof=1.2
q=[pop_density[i] for i in N]
p=1000
ablty=cof*pop_sum/p

geo_dis={(i,j):np.hypot(demandCoordinates[i][0]\
    -demandCoordinates[j][0],
    demandCoordinates[i][1]\
        -demandCoordinates[j][1]) for i,j in A}   # 几何距离
# od=np.load("杭州ODN.npy")
od=np.load("杭州mergedOD.npy")   # np格式的od矩阵
od_dis={(i,j):od[i][j] for i,j in A}  # 字典格式的od矩阵
dis=od_dis

mdl=Model("p-center")
x=mdl.addVars(A,vtype=GRB.CONTINUOUS,ub=1,lb=0)
# x=mdl.addVars(A,vtype=GRB.BINARY)
n=mdl.addVars(N,vtype=GRB.INTEGER)
mdl.update()

mdl.ModelSense=GRB.MINIMIZE
mdl.setObjective(quicksum(x[i,j]*dis[i,j]*q[j]\
     for i,j in A))

mdl.addConstrs(quicksum(x[i,j] for j in N)== 1 for i in N);

mdl.addConstr(quicksum(n[i] for i in N )== p);

mdl.addConstrs((quicksum(q[i]*x[i,j] for i in N)<=n[j]*ablty )\
    for j in N);

mdl.optimize()

# 画所有点及标注需求
markersize=3
linewidth=0.5
for i in N:
    xy=demandCoordinates[i]
    plt.plot(xy[0],xy[1],c="b",\
        marker="s",markersize=markersize)
    #plt.text(xy[0],xy[1],f"{q[i]}")
norm=color.Normalize(vmax=13,vmin=0)
# 画需求量
for i in N:
    if (n[i].x>0):
        xy=demandCoordinates[i]
        col=plt.cm.rainbow
        nMax=0.0
        for ni in N:
            # print(type(n[ni].x),n[ni].x,type(nMax))
            if n[ni].x>nMax:
                nMax=n[ni].x
        # norm=color.Normalize(vmax=round(nMax)+1,vmin=0)
        plt.plot(xy[0],xy[1],marker="s",\
            color=col(norm(n[i].x)),markersize=markersize)
        # plt.text(xy[0]-5,xy[1]-5,f"{n[i].x}",color="b")
        

# 画供应线
for i,j in A:
    if x[i,j].x>0.0:
        demandCoordinates[i][0],demandCoordinates[i][1]
        demandCoordinates[j][0],demandCoordinates[j][1]
        plt.plot([demandCoordinates[i][0],\
            demandCoordinates[j][0]]\
            ,[demandCoordinates[i][1],\
            demandCoordinates[j][1]],\
            color="r",linewidth=linewidth)

plt.xlabel("x")
plt.ylabel("y")
plt.show()

array=np.array([])
for i in N:
    array=np.append(array,n[i].x)
array
np.save("n.npy",array)

array2=np.zeros((size,size))
for i,j in A:
    array2[i,j]=x[i,j].x
np.save("x.npy",array2)




