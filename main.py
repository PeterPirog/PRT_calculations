import SPRT_functions as SPRT
import GTC
import GTCext
import numpy as np


term1=SPRT.PRT(model='5685',numer='1114')


#term1.R0.x=102

T=GTC.ureal(29.764663066392302,0.005,label='temp')
W=GTC.ureal(1.11813889,1.982113655829038e-05,label='W')

#print(SPRT.Conv_kelvin2celsius(T))
#SPRT.Calculate_Wr(T,verbose=True)
#SPRT.Calculate_temp_from_W(W,verbose=True)



value_list=[[1,2,3,4],[5,6,7,8]]

#unc_list=[[0.1,0.2,0.3,0.4],[0.01,0.02,0.03,0.04]] #osobna niepwenośc dla każdej wartości
unc_list=0.1  # jedna niepewnośc dla wszystkich wartości

value_list=np.array(value_list)
unc_array=SPRT.lists2unc_array(value_list,unc_list,k=2,)

print('value_list=\n',value_list)
print('unc_list=\n',unc_list)
print('unc_array=\n',unc_array) # tutaj jest wytworzona macierz liczb z niepewnoscią
print('sin(unc_array)=\n',GTC.sin(unc_array)) #tutaj można zrobic ich sinus

#print(SPRT.Calculate_temp_from_W(1.0794875093598515))

