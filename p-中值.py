# -*- coding: utf-8 -*-
import math
import random
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']  # 添加这条可以让图形显示中文

#分隔

#计算路径距离，即评价函数
def calFitness(chrom,dis_matrix, cnum, d, c):
    #cnum:备选点数量
    #d:需求量列表，对应demandCoordinates
    #c:
    dis_sum = 0#总距离
    dis = 0#距离
    declist = []#位置坐标
    dec_chrom =chrom.copy()#对应坐标
    d_list = [[] for i in range(cnum)]#列出每个
    weight = [0 for i in range(cnum)]
    demand = [0 for i in range(cnum)]
    for i in range(cnum):
        if chrom[i] >= 1:
            for j in range(chrom[i]):
                declist.append(i)
    
    for i in range(cnum,len(dec_chrom)):
        dec_chrom[i] = declist[dec_chrom[i]-1]
        d_list[dec_chrom[i]].append(i-cnum)
        weight[dec_chrom[i]] += dis_matrix.loc[i-cnum,dec_chrom[i]]
        demand[dec_chrom[i]] += d[i-cnum]
    
    dis_sum = 0 
    for i in range(len(demand)):
        if demand[i] > c[i]:
            dis_sum += (demand[i]-c[i])*1000
    dis_sum += sum(weight)
    return round(dis_sum,1)


def traversal_search(chrom,dis_matrix,tabu_list, cnum, d, c, p):
    #邻域随机遍历搜索，成对交换+单点变异
    traversal = 0#搜索次数
    traversal_list = []#存储局部搜索生成的解,也充当局部禁忌表
    traversal_value = []#存储局部解对应路径距离
    while traversal <= traversalMax:
        new_chrom = chrom.copy()#复制当前路径，并交换生成新路径
        pos1,pos2 = random.randint(0, cnum-1),random.randint(0, cnum-1)#交换点
        new_chrom[pos1],new_chrom[pos2]=new_chrom[pos2],new_chrom[pos1]
        
        pos1,pos2 = random.randint(cnum,len(chrom)-1),random.randint(cnum,len(chrom)-1)#交换点
        new_chrom[pos1],new_chrom[pos2]=new_chrom[pos2],new_chrom[pos1]
        
        for i in range(cnum,len(chrom)):
            if random.random() > 0.2:#一定概率改变
                new_chrom[i] = random.randint(1,p)
                
        new_value = calFitness(new_chrom,dis_matrix, cnum, d, c)#当前路径距离
        #新生成路径不在全局禁忌表和局部禁忌表中，为有效搜索，否则继续搜索
        if (new_chrom not in traversal_list) & (new_chrom not in tabu_list):
            traversal_list.append(new_chrom)
            traversal_value.append(new_value)
            traversal += 1
    
    return min(traversal_value),traversal_list[traversal_value.index(min(traversal_value))]
    
    
def initialize(dnum, cnum , p):
    """
    in:dnum-需求点数量，cnum-备选点数量，
    out:染色体
    """
    clist = [random.randint(0,cnum-1) for i in range(p)]
    cchrom = [clist.count(i) for i in range(cnum) ]
    dchrom = [random.choice(range(1,p+1)) for i in range(dnum)]
    chrom = cchrom + dchrom
    
    return chrom
    
    
#画散点图
def draw_sca(Coordinates1,Coordinates2):
    x,y= [],[]
    
    x = [i[0] for i in Coordinates1]
    y = [i[1] for i in Coordinates1]
    plt.scatter(x, y, color='#ff69E1', marker='o')
    
    x = [i[0] for i in Coordinates2]
    y = [i[1] for i in Coordinates2]
    plt.scatter(x, y, color='#4169E1', marker='*')
    
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()


#画分布图
def draw_path(chrom, demandCoordinates, centerCoordinates, p, cnum):
    centerlist = []
    for i in range(cnum):
        if chrom[i] >= 1:
            for j in range(chrom[i]):
                centerlist.append(centerCoordinates[i])
    print(centerlist)
    for i in range(cnum,len(chrom)):
        if chrom[i] >= 1:
            plt.plot([centerlist[i][0],demandCoordinates[i-cnum][0]], [centerlist[0][1],demandCoordinates[i-cnum][1]], 'r-', color='#4169E1', alpha=0.8, linewidth=0.8)#plt.plot([x1,x2],[y1,y2])
    draw_sca(demandCoordinates,centerCoordinates)


if __name__ == '__main__':
    #参数
    CityNum = 50#城市数量
    MinCoordinate = 0#二维坐标最小值
    MaxCoordinate = 100#二维坐标最大值
    
    #TS参数
    tabu_limit = 200 #禁忌长度
    iterMax = 2000#迭代次数
    traversalMax = 100#每一代局部搜索次数
    
    tabu_list = [] #禁忌表
    tabu_time = [] #禁忌次数
    best_value = math.pow(10,10)#较大的初始值，存储最优解
    best_line = []#存储最优路径
    
    ablty=4;
    
    #需求点位置及需求量，备选中心位置及能力
    demandCoordinates = [(88, 16),(25, 76),(69, 13),(73, 56),(80, 100),(22, 92),(32, 84),(73, 46),(29, 10),(92, 32),(44, 44),(55, 26),(71, 27),(51, 91),(89, 54),(43, 28),(40, 78),(60,66)]
    print(len(demandCoordinates))
    centerCoordinates = demandCoordinates
    d = [1,2,1,3,5,3,4,6,2,1,3,4,1,2,6,1,4,2]#需求量，对应demandCoordinates
    c = [ablty for i in range(len(d))]#能力都设置为25，对应centerCoordinates
    draw_sca(demandCoordinates,centerCoordinates)#位置图
    
    p = round(sum(d)/ablty)+1 #待决策物流中心数量
    dnum = len(demandCoordinates) #需求点数量
    cnum = len(centerCoordinates) #备选中心数量
    
    
    # 计算中心与需求点之间的距离
    dis_matrix = pd.DataFrame(data=None,columns=range(cnum),index=range(dnum))
    for i in range(dnum):
        xi,yi = demandCoordinates[i][0],demandCoordinates[i][1]
        for j in range(len(centerCoordinates)):
            xj,yj = centerCoordinates[j][0],centerCoordinates[j][1]
            dis_matrix.iloc[i,j] = round(math.sqrt((xi-xj)**2+(yi-yj)**2),2)
    
    
    # 初始化,随机构造
    num = 50
    chroms = [initialize(dnum, cnum, p) for i in range(num)]
    values = [calFitness(chrom,dis_matrix, cnum, d, c) for chrom in chroms]
    print(values)
    best_value = min(values)
    best_chrom = chroms[values.index(best_value)]
    chrom,value = best_chrom,best_value
    
    # 存储当前最优
    print('初代最优值 %.1f' % (best_value))
    
    best_value_list = []
    best_value_list.append(best_value)
    #更新禁忌表
    tabu_list.append(best_chrom)
    tabu_time.append(tabu_limit)
    
    itera = 0
    while itera <= iterMax:
        new_value,new_chrom = traversal_search(chrom,dis_matrix,tabu_list, cnum, d, c, p)
        if new_value < best_value:#优于最优解
            best_value,best_chrom = new_value,new_chrom#更新最优解
            best_value_list.append(best_value)
            print('第%.d代最优值 %.1f' % (itera,best_value))
        chrom,value = new_chrom,new_value#更新当前解
        
        #更新禁忌表
        tabu_time = [x-1 for x in tabu_time]
        if 0 in tabu_time:
            tabu_list.remove(tabu_list[tabu_time.index(0)])
            tabu_time.remove(0)
        
        tabu_list.append(chrom)
        tabu_time.append(tabu_limit)
        itera +=1
    #画图
    draw_path(best_chrom, demandCoordinates, centerCoordinates, p, cnum)
