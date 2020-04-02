
#calculation a,b,c coefficient in range 7 from 0.01 C to 660.323 C
# with no uncertainties,
import ITS90
import GTC
import GTCext
import numpy as np

# STEP 1 -  DATA FROM CERTIFICATE
Wt = np.array([3.37543469, 2.56855103, 1.89259628])
t = [660.323, 419.527, 231.928]
ut = [0.004, 0.0017, 0.0015]

t = GTCext.urealext(value_list=t, unc_list=ut, k=2, array_label='t', df=GTC.inf)
print('t=', t)

Wt = GTCext.urealext(value_list=Wt, array_label='Wt')
print('\nW(t)=', Wt)

Wrt=GTCext.calculate_func_from_UncertainArray(ITS90.calculate_Wr_unc,t)
print('\nWr(t)=', Wrt)


deltaW=Wt-Wrt

print('\nW(t)-Wr(t)=',deltaW)


A=ITS90.create_Wt1_array(Wt)
print('\nA=',A)
B=np.reshape(deltaW,(-1,1))
print('\nB=',B)

#STEP 2 - CALCULATING a,b,c ITS-90 coefficients


invA=GTCext.inv(A)
print('\ninvA=',invA)

coeff=GTC.la.matmul(invA,B)
print('\ncoeff=',coeff)

a=coeff[0][0]
b=coeff[1][0]
c=coeff[2][0]

print('\nCalculated coefficients:\n')
print('a coeff=',a.x,'u=',a.u)
print('b coeff=',b.x,'u=',b.u)
print('c coeff=',c.x,'u=',c.u)

#### STEP 3-   TEMPERATURE CALCULATION FROM RESISTANCE MEASURED
#resistancec from measurement

R0=GTC.ureal(100,0.000002,label='R0') #Triple point of water resistance
Ri=[102,189,300] # measured resistances
R=GTCext.urealext(value_list=Ri, unc_list=0.0005, k=2, array_label='R', df=GTC.inf)
print('\nR0=',R0)
print('\nR=',R)
Wt=R/R0 # calculating reference function for measured resistances
print('\nW(t)=',Wt)



Wt1=GTCext.python_list_transposition(Wt-1)

pow2=lambda
#Wt2=GTC.pow(Wt1,2)
#Wt3=GTC.pow(Wt1,3)

print('\nWt1',Wt1)
#print('\nWt2',Wt2)
#print('\nWt3',Wt3)


"""
Wrt=GTCext.calculate_func_from_UncertainArray(ITS90.calculate_Wr_unc,t)
print('\nWr(t)=',Wrt)

print('Calculated W(t)=',Wt)
Wt1_array=ITS90.create_Wt1_array(Wt)
Wt=np.reshape(Wt,(-1,1))
print('Wt1_array=',Wt1_array)

print('coeff=',coeff)

delta_Wt_Wrt=np.matmul(Wt1_array,coeff)
print('W(r)-Wr(t)=',delta_Wt_Wrt)
Wr=Wt-delta_Wt_Wrt
print('Wr(t)=',Wr)

#Convertt Wr(t) to temperature
t_calculated=np.array(list(map(ITS90.calculate_temp_from_Wr,Wr)))

print('t calculated=',t_calculated)

"""