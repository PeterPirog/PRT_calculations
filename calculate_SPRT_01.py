import GTC

import GTCext
import ITS90

#Funkcja rezystancji zredukowanej W(t) ze świadectwa wzorcowania
Wt=[4.28556295,3.37543469,2.56855103,1.89259628]
#zamiana funkcji na tablicę z niepewnościami

Wt=GTCext.urealext(value_list=Wt, unc_list=0.0, k=2, array_label='Wt', df=GTC.inf)
print('W(t)=',Wt)