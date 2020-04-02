import GTC

import GTCext
import ITS90

# Funkcja rezystancji zredukowanej W(t) ze świadectwa wzorcowania
Wt = [4.28556295, 3.37543469, 2.56855103, 1.89259628]
# zamiana funkcji na tablicę z niepewnościami

Wt = GTCext.urealext(value_list=Wt, unc_list=0.0, k=2, array_label='Wt', df=GTC.inf)
print('W(t)=', Wt)

# Wprowadzenie temperatur ze świadectwa
t = [961.78, 660.323, 419.527, 231.928]
ut = [0.0052, 0.004, 0.0017, 0.0015]
t = GTCext.urealext(value_list=t, unc_list=ut, k=2, array_label='t', df=GTC.inf)
print('t=', t)

#Function for calculating function from UncertaintyArray type
Wrt = GTCext.calculate_func_from_UncertainArray(ITS90.calculate_Wr,t)
print(Wrt)
print(t)
print('Wr(t)=',Wrt)
print('W(t)=',Wt)
print('W(t)-Wr(t)',Wt-Wrt)