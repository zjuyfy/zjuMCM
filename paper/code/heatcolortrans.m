%将彩色热力图转化为黑白,传给heat2data函数进行识别

workingdtr='C:\Users\heyiyang\Desktop\建模\程序\paper\pic\';%工作目录
dataim=imread([workingdtr,'zh人口.png']);
workim=rgb2hsv(dataim);
[x,y,z]=size(workim);
datax=1:x;%x坐标
datay=1:y;%y坐标
