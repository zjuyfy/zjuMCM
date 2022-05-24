
data=readNPY('nyod.npy');
xy=readNPY('nyxy.npy');
tol_dis=40;

workmat=[data,xy];
[l,bin]=size(workmat);
judge=find(sum(workmat==0)>l/2);
workmat(judge,:)=[];
workmat(:,judge)=[];
p=workmat<tol_dis;
i=1;
j=1;
while i<=l
    j=i+1;
    while j <= l
        if p(j,i)   
            workmat(j,:)=[];
            workmat(:,j)=[];
        end
        [l,bin]=size(workmat);
        j=j+1;
    end
    i=i+1;
end
writeNPY(workmat(:,1:end-2),'nymergedOD.npy')
writeNPY(workmat(:,end-1:end),'nymergedXY.npy')

