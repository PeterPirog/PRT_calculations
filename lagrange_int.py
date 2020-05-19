import GTC
import GTCext
from functools import reduce
import numpy as np


def lagrange_productsK(X,x,k):
    N = X.shape[1]
    lag_prod = [1 if k==i else (x - X[0, i]) / (X[0, k] - X[0, i]) for i in range(N)]
    prod= reduce((lambda x, y: x * y), lag_prod)
    return prod

def calculate_lagrange_val(X_array,Y_array,x):
    N = X_array.shape[1]
    Px_list = [Y_array[0, k] * lagrange_productsK(X_array, x, k) for k in range(N)]
    Px = reduce((lambda x, y: x + y), Px_list)
    return Px



#TEST

X=GTCext.urealext(value_list=[1,2,3,4,5,6], unc_list=0.1, k=2, array_label='X', df=GTC.inf)
Y=GTCext.urealext(value_list=[2,3,3,4,2,1], unc_list=0.1, k=2, array_label='Y', df=GTC.inf)

#Single value
x=2
Px=calculate_lagrange_val(X,Y,x)
print('P(x)=',Px,' for x=',x)
#Single vector
x=np.arange(1,6,0.1)
y=[calculate_lagrange_val(X,Y,x[i]) for i in range(len(x))]
yx=[y[i].x for i in range(len(x))]
print(x)
print(y)
print(y,yx)

import matplotlib.pyplot as plt
plt.plot(x,yx)
plt.ylabel('some numbers')
plt.show()


