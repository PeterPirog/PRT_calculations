import GTC

import GTCext


x=GTCext.urealext(value_list=[1,2,3,4,5,6], unc_list=0.1, k=2, array_label='x', df=GTC.inf)
y=GTCext.urealext(value_list=[2,3,7,4,2,1], unc_list=0.1, k=2, array_label='y', df=GTC.inf)

print('x=',x)
print('y=',y)

N=x.shape[1]
print(N)
z=x/y
print('z=',z)