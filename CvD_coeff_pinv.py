import numpy as np

import GTC
from GTC import  la, ureal
from  GTCext import  psolve,pinv, urealext
from scipy.optimize import curve_fit


A=np.array([[1,2,3],[4,5,6]])
B=la.uarray([[-11,2],[2,3],[2,-1]])



a=la.uarray([[-2,3],[-4,1]])
b=la.uarray([4,-2])
print('Solving 1:',psolve(a,b))


a=la.uarray([[-2,3],[-4,1],[1,1]])
b=la.uarray([4,-2,2.8])
print('Solving 2:',psolve(a,b))


au=la.uarray([[ureal(-2,0.1),ureal(3,0.1)],[ureal(-4,0.1),ureal(1,0.1)],[ureal(1,0.1),ureal(1,0.1)]])
bu=la.uarray([ureal(4,0.1),ureal(-2,0.1),ureal(2.8,0.1)])
print('Solving 3:',psolve(au,bu))


#C=urealext(value_list=[[-2,3],[-4,1],[1,1]], unc_list=[[2,3],[4,1],[1,1]], k=1, array_label='X', df=GTC.inf)
#print("C=",C)

R0=ureal(100,0.0)
R = [67.7848, 84.5387, 100.1399, 189.513, 257.2021, 337.9695]
UR=[0.0109,0.0099,0.0098,0.0106,0.0165,0.0071]

T = [-80.0078, -38.8397, 0, 231.9287, 419.5246, 660.323]
UT=[0.027,0.025,0.025,0.029,0.048,0.022]

R=urealext(value_list=R, unc_list=UR, k=2, array_label='R', df=GTC.inf)
print("R=",R)
T=urealext(value_list=T, unc_list=UT, k=2, array_label='T', df=GTC.inf)

Rs=R/R0-1
Rs=np.transpose(Rs)
print("Rs=",Rs)
print("Rs shape=",Rs.shape)


N=len(UR)
print("N=",N)
print("type:",type(R))

object_methods = hasattr(R,"method")


print(dir(R))
print(R.shape[1])


#T=np.array([1,2,3,4,5])
T2=GTC.pow(T,2)
T3=(T-100)*GTC.pow(T,3)
#T3=GTC.pow(T,3)
print("T=",T)
print("T2=",T2)
print("T3=",T3)

Ts=np.vstack((T,T2,T3)).transpose()
print("Ts=",Ts)

print(Ts.shape)

W=psolve(Ts,Rs)
print("\nw=",W)
A=W[0]
B=W[1]
C=W[2]
print("\nA=",A)
print("\nB=",B)
print("\nC=",C)