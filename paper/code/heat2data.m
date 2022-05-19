
workingdtr='';
workim=imread([workingdtr,'人口热力图-work.png']);
cpim=imread([workingdtr,'人口热力图-ovf.png']);

%-------对准坐标系
%由于坐标系均为直角坐标系，且y轴方向均为北方，所以只有四个自由度X'=SX+V，也就是说只需要两个二维点即可确定坐标系变换
%注意选的点不能太近
syms sx sy vx vy
s=[sx,0;0,sy,];%伸缩
v=[vx,vy];%平移
p1=[498471.0 3342937.8483];%基准点[57]
p2=[532472.0 3341447.9522];%基准点[-1]
p3=[520953.0 3335486.6781];%检验点，用来判断误差多大[2189]
imshow(cpim)%比较，选出坐标点
x1=[24.3947,288.7591];
x2=[542.7264,310.7756];
x3=[366.5943,398.2127];
[Sx,Sy,Vx,Vy]=solve([x1*s+v==p1,x2*s+v==p2],[sx,sy,vx,vy]);
V=double([Vx,Vy]);
S=double([Sx,0;0,Sy]);
Error=(x3*S+V-p3)/sum(p3-p2);
if sum(abs(Error))>0.01
    warning('误差超过了1%！')
    Error
end

data=readNPY("杭州mergedXY.npy");

dataxy=data;%输入要读取的点的坐标数据
dataheat=[];

for i=1:length(dataxy)
    X=(dataxy(i,:)-V)*inv(S)
    if X(1)<0|X(2)<0
        dataheat=[dataheat;0];
        continue
    end
    dataheat=[dataheat;255-workim(round(X(2)),round(X(1)),1)];
end
%输出数据
writeNPY(dataheat,"dataheat.npy")

