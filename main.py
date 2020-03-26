import SPRT_functions as SPRT
import GTC


term1=SPRT.PRT(model='5685',numer='1114')


#term1.metoda1()
#term2.metoda1()

#term1.R0.x=102

T=GTC.ureal(29.764663066392302,0.005,label='temp')
W=GTC.ureal(1.11813889,1.982113655829038e-05,label='W')

#print(SPRT.Conv_kelvin2celsius(T))
#SPRT.Calculate_Wr(T,verbose=True)
#SPRT.Calculate_temp_from_W(W,verbose=True)

value_list=[[1,2,3,4],[5,6,7,8]]
unc_list=[[0.1,0.2,0.3,0.4],[0.01,0.02,0.03,0.04]]

unc_array=SPRT.lists2unc_array(value_list,unc_list)
print(unc_array)


#print(SPRT.Calculate_temp_from_W(1.0794875093598515))
