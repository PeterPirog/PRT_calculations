
#calculation a,b,c coefficient in range 7 from 0.01 C to 660.323 C
# with no uncertainties,
import ITS90
import numpy as np

# STEP 1 -  DATA FROM CERTIFICATE
Wt = np.array([3.37543469, 2.56855103, 1.89259628])
t = np.array([660.323, 419.527, 231.928])
Wrt=np.array(list(map(ITS90.calculate_Wr,t)))
deltaW=Wt-Wrt


print('Wr(t)=',Wrt)
print('W(t)=',Wt)
print('W(t)-Wr(t)=',deltaW)


A=ITS90.create_Wt1_array(Wt)
print('A=',A)
B=np.reshape(deltaW,(-1,1))
print('B=',B)

#STEP 2 - CALCULATING a,b,c ITS-90 coefficients
pinvA=np.linalg.pinv(A)
coeff=np.matmul(pinvA,B)
print('coeff=',coeff)
a=coeff[0][0]
b=coeff[1][0]
c=coeff[2][0]

print('\nCalculated coefficients:\n')
print('a coeff=',a)
print('b coeff=',b)
print('c coeff=',c)

#### STEP 3-   TEMPERATURE CALCULATION FROM RESISTANCE MEASURED
#resistancec from measurement

R0=100 #Triple point of water resistance
Ri=[102,189,300] # measured resistances
Ri=np.array(Ri)
Wt=Ri/R0 # calculating reference function for measured resistances

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