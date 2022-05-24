function dy=logistic(t,y)
p1=0.24; p2=0.87; r1=0.5; r2=0.04; N1=40500e4; N2=40500e4;
dy=zeros(2,1);
dy(1)=r1 *y(1).*(1-y(1)./N1-p1*y(2)./N2); 
dy(2)=r2 *y(2).*(1-y(2)./N2-p2*y(1)./N1); 
