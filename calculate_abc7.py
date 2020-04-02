
#calculation a,b,c coefficient in range 7 from 0.01 C to 660.323 C
# with no uncertainties,
import ITS90


import numpy as np
Wt = np.array([3.37543469, 2.56855103, 1.89259628])
t = np.array([660.323, 419.527, 231.928])
Wrt=np.array(list(map(ITS90.calculate_Wr,t)))
deltaW=Wt-Wrt
Wt1=np.reshape(Wt-1,(-1,1))
Wt1_pow2=np.reshape(Wt1**2,(-1,1))
Wt1_pow3=np.reshape(Wt1**3,(-1,1))

print('Wr(t)=',Wrt)
print('W(t)=',Wt)
print('W(t)-Wr(t)=',deltaW)
print('W(t)-1=',Wt1)

A=np.hstack((Wt1,Wt1_pow2,Wt1_pow3))
print('A=',A)
B=np.reshape(deltaW,(-1,1))
print('B=',B)

pinvA=np.linalg.pinv(A)
coeff=np.matmul(pinvA,B)
print('coeff=',coeff)
