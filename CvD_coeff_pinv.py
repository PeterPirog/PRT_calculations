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


C=urealext(value_list=[[-2,3],[-4,1],[1,1]], unc_list=0.01, k=2, array_label='X', df=GTC.inf)
print("C=",C)