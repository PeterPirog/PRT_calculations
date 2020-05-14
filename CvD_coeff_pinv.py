import numpy as np

from GTC import  la
from scipy.optimize import curve_fit


A=np.array([[1,2,3],[4,5,6]])
B=la.uarray([[-11,2],[2,3],[2,-1]])

B=np.array([[-11,2],[2,3],[2,-1]])

Bt=la.transpose(B)
BtB=la.matmul(Bt,B)
invBtB=la.inv(BtB)
pinvB=la.matmul(invBtB,Bt)
#pinvB=la.matmul(Bt,B)
#pinvB=la.inv(pinvB)
#pinvB=la.matmul(pinvB,Bt)

#A+=(AtxA)-1 At
def pinv(GTC_array):
    B=GTC_array
    Bt = la.transpose(B)
    BtB = la.matmul(Bt, B)
    invBtB = la.inv(BtB)
    pinvB = la.matmul(invBtB, Bt)
    return pinvB

def psolve(A,B):
    pinvA=pinv(A)
    result=la.matmul(pinvA,B)
    return result

print("matrix:",B)
print("GTC result:",pinv(B))

print("numpy result:",np.linalg.pinv(B))

a=la.uarray([[-2,3],[-4,1]])
b=la.uarray([4,-2])

print('Solving 1:',psolve(a,b))

a=la.uarray([[-2,3],[-4,1],[1,1]])
b=la.uarray([4,-2,2.8])

print('Solving 2:',psolve(a,b))
