clear
txt = ['Hg';'Ga';'In';'Sn';'Zn';'Al']
txt2=['W(n)','t(n)']


sig = x_mdialog('Wprowadz wartosci w punktach',txt,txt2,['0.84347','-38.8344';'1.118138893','29.7646';'1.60980184811','156.5985';'1.89259628','231.928';'2.56855103','419.527';'3.37543469','660.323'])


WHg =strtod(sig(1,1))
WGa =strtod(sig(2,1))
WIn=strtod(sig(3,1))
WSn=strtod(sig(4,1))
WZn=strtod(sig(5,1))
WAl=strtod(sig(6,1))
tHg = strtod(sig(1,2))
tGa = strtod(sig(2,2))
tIn=strtod(sig(3,2))
tSn=strtod(sig(4,2))
tZn=strtod(sig(5,2))
tAl=strtod(sig(6,2))

i=0
A=[-2.13534729,3.1832472,-1.80143597,0.71727204,0.50344027,-0.6189939,-0.05332322,0.28021362,0.10715224,-0.29302865,0.04459872,0.11868632,-0.05248134]
C=[2.78157254,1.64650916,-0.1371439,-0.00649767,-0.00234444,0.00511868,0.00187982,-0.00204472,-0.00046122,0.00045724]


sum1 = 0
for i = 2 : 13
sum1 = sum1 + A(:,i) * ((log((tHg + 273.15) / 273.16) + 1.5) / 1.5) ^ (i-1);
end
Wr_t1 = exp(A(:,1) + sum1)


sum2 = 0
for i = 2 : 10
sum2 = sum2 + C(:,i) * ((tGa / 481) - 1) ^ (i-1);
end
Wr_t2 = C(:,1) + sum2

sum3 = 0
for i = 2 : 10
sum3 = sum3 + C(:,i) * ((tIn / 481) - 1) ^ (i-1);
end
Wr_t3 = C(:,1) + sum3

sum4 = 0
for i = 2 : 10
sum4 = sum4 + C(:,i) * ((tSn / 481) - 1) ^ (i-1);
end
Wr_t4 = C(:,1) + sum4

sum5 = 0
for i = 2 : 10
sum5 = sum5 + C(:,i) * ((tZn / 481) - 1) ^ (i-1);
end
Wr_t5 = C(:,1) + sum5

sum6 = 0
for i = 2 : 10
sum6 = sum6 + C(:,i) * ((tAl / 481) - 1) ^ (i-1);
end
Wr_t6 = C(:,1) + sum6


M=[WHg-1,(WHg-1)^2;WGa-1,(WGa-1)^2]
Y=[WHg-Wr_t1;WGa-Wr_t2]
ab=inv(M)*Y

M1=[WGa-1]
Y1=[WGa-Wr_t2]
a=inv(M1)*Y1

M2=[WIn-1]
Y2=[WIn-Wr_t3]
a1=inv(M2)*Y2

M3=[WIn-1,(WIn-1)^2;WSn-1,(WSn-1)^2]
Y3=[WIn-Wr_t3;WSn-Wr_t4]
ab2=inv(M3)*Y3

M3=[WSn-1,(WSn-1)^2;WZn-1,(WZn-1)^2]
Y3=[WSn-Wr_t4;WZn-Wr_t5]
ab3=inv(M3)*Y3

M4=[WSn-1,(WSn-1)^2,(WSn-1)^3;WZn-1,(WZn-1)^2,(WZn-1)^3;WAl-1,(WAl-1)^2,(WAl-1)^3]
Y4=[WSn-Wr_t4;WZn-Wr_t5;WAl-Wr_t6]
ab4=inv(M4)*Y4


Wy=tlist(['v','-38 C do 30 ',' 0 - 30', '0 - 157', '0 - 232','0-420','0-660' ],ab,a,a1,ab2,ab3,ab4)

tree_show(Wy)


