t0=0;tf=10;
[t,y]=ode45('logistic',[t0 tf],[784e4 25462e4]);%取初始条件一时， 求微分方程数值解
subplot(1 ,1,1); 
plot(t,y(:,1),t,y(:,2),'r');%画出x1(t),x2(t)曲线图
xlabel('年份序号（2022年起）');
ylabel('保有量/万辆');
gtext('电动汽车');
gtext('燃油汽车');%作标记
title('电动汽车与燃油汽车未来十年保有量预测');
grid on; 