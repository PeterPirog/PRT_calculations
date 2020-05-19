import GTC

import GTCext


X=GTCext.urealext(value_list=[1,2,3,4,5,6], unc_list=0.1, k=2, array_label='X', df=GTC.inf)
Y=GTCext.urealext(value_list=[2,3,7,4,2,1], unc_list=0.1, k=2, array_label='Y', df=GTC.inf)
"""
print('X=',X)
print('Y=',Y)

N=X.shape[1]

"""
from functools import reduce

def lagrange_productsK(X,x,k):
    N = X.shape[1]
    print('N=',N)
    #lag_prod = [i for i in range(N)]
    #lag_prod=[(x-X[0,i])/(X[0,k]-X[0,i]) for i in range(N) if k is not i else 1]
    #[unicode(x.strip()) if x is not None else '' for x in row]
    lag_prod = [1 if k==i else (x - X[0, i]) / (X[0, k] - X[0, i]) for i in range(N)]
    print('lag_prod=', lag_prod)
    #prod=[lag_prod[0] if i==0 else prod[i-1]*prod[i] for i in range(N)]
    prod= reduce((lambda x, y: x * y), lag_prod)
    print('prod=',prod)
    return prod
"""
prod=lagrange_productsK(X,1.5,2)
print(prod)
x=5
Px_list=[Y[0,k]*lagrange_productsK(X,x,k) for k in range(N)]
print('Px_list=',Px_list)

Px= reduce((lambda x, y: x + y), Px_list)
print('P(x)=',Px,' for x=',x)
"""
def calculate_lagrange_val(X_array,Y_array,x):
    N = X_array.shape[1]
    Px_list = [Y_array[0, k] * lagrange_productsK(X_array, x, k) for k in range(N)]
    Px = reduce((lambda x, y: x + y), Px_list)
    return Px

X=GTCext.urealext(value_list=[1,2,3,4,5,6], unc_list=0.1, k=2, array_label='X', df=GTC.inf)
Y=GTCext.urealext(value_list=[2,3,7,4,2,1], unc_list=0.1, k=2, array_label='Y', df=GTC.inf)
x=2
Px=calculate_lagrange_val(X,Y,x)
print('P(x)=',Px,' for x=',x)



