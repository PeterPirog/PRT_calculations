import numpy as np

import ITS90 as SPRT_1

from GTC import *

import matplotlib.pyplot as plt
########################### example data ########################
T1=ureal(231.928,0.0015)
T2=ureal(419.527,0.0017)
T3=ureal(660.323,0.0040)
T4=ureal(961.780,0.0052)

Rtpw=ureal(2.5534637,0.0000041)
Rtpw_fac=2.5534637/Rtpw
#Rtpw_fac=1
WH2O=1*Rtpw_fac
WSn=1.89259628*Rtpw_fac
WZn=2.56855103*Rtpw_fac
WAl=3.37543469*Rtpw_fac
WAg=4.28556295*Rtpw_fac

Wr_Sn=SPRT_1.calculate_Wr_unc(T1)
Wr_Zn=SPRT_1.calculate_Wr_unc(T2)
Wr_Al=SPRT_1.calculate_Wr_unc(T3)
Wr_Ag=SPRT_1.calculate_Wr_unc(T4)

#########################calculating deviation function coefficients#############
WFP_array=la.uarray([[WSn],[WZn],[WAl]])
Wr_array=la.uarray([[Wr_Sn],[Wr_Zn],[Wr_Al]])
M_array=la.uarray([[WSn-1,(WSn-1)**2,(WSn-1)**3],[WZn-1,(WZn-1)**2,(WZn-1)**3],[WAl-1,(WAl-1)**2,(WAl-1)**3]])
Y_array=WFP_array-Wr_array

A=la.solve(M_array,Y_array)

#######################Temperature calculating function in range 0,01 + 660##############
R_range=np.arange(2.5534637,8.61904995263575,0.1)#0.0046 refers to 0,5 C; 0,1 for fast computing
R_unc=ureal(0,0.000012)
R_range_unc=R_range+R_unc


def Temp_res_a7(res,TPW,a,b,c):
    l = int(len(res))
    Temps=la.ones((1,l))
    for i in range(l):
        W = res[i] / TPW
        dW = a * (W - 1) + b * pow((W - 1), 2) + c * pow((W - 1), 3)
        WR = dW + W
        Temp = SPRT_1.calculate_temp_from_Wr(WR)
        Temps[0, i] = Temp
    return Temps


T_calc=Temp_res_a7(R_range_unc,Rtpw,A[0],A[1],A[2])

######### conversion from GTC uarray to list (plottable vectors)##########
def matrix_float(mat):
    l = int(len(la.transpose(mat)))
    floats=la.ones((1,l))
    for i in range(l):
        floats[0, i] = float((mat[0,i]))
    return floats
Ut_table=(matrix_float(uncertainty(T_calc)))
Ttable=(matrix_float(value(T_calc)))

X=list(Ut_table)
Y=list(Ttable)

plt.plot(Y,X,'ro')
plt.ylabel('uncertainty K')
plt.xlabel('Temperature K')
plt.show()

























