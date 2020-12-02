import numpy as np
import math
import ITS90 as SPRT_1

from GTC import *

import matplotlib.pyplot as plt
########################### example data ########################

T1=ureal(-189.3442,0.0012)
T2=ureal(-38.8344,0.0010)
T3=ureal(231.928,0.0015)
T4=ureal(419.527,0.0017)

Rtpw=ureal(25.558080,0.000056)
Rtpw_fac=25.558080/Rtpw
#Rtpw_fac=1
WH2O=1*Rtpw_fac
WAr=0.21599336*Rtpw_fac
WHg=0.84416637*Rtpw_fac
WSn=1.89261334*Rtpw_fac
WZn=2.56857963*Rtpw_fac

Wr_Ar=SPRT_1.calculate_Wr_unc(T1)
Wr_Hg=SPRT_1.calculate_Wr_unc(T2)
Wr_Sn=SPRT_1.calculate_Wr_unc(T3)
Wr_Zn=SPRT_1.calculate_Wr_unc(T4)

c=1
#########################calculating deviation function coefficients#############
if c==1:
    WFP_array=la.uarray([[WAr],[WHg]])
    Wr_array=la.uarray([[Wr_Ar],[Wr_Hg]])
    M_array=la.uarray([[WAr-1,(WAr-1)*log(WAr)],[WHg-1,(WHg-1)*log(WHg)]])
    Y_array=WFP_array-Wr_array
else:
    WFP_array = la.uarray([[WSn], [WZn]])
    Wr_array = la.uarray([[Wr_Sn], [Wr_Zn]])
    M_array = la.uarray([[WSn - 1, (WSn - 1)**2], [WZn - 1, (WZn - 1)**2]])
    Y_array = WFP_array - Wr_array

A=la.solve(M_array,Y_array)
print(A)

#######################Temperature calculating function in range 0,01 + 660##############
if c==1:
    R_range = np.arange(5.52038, 25.558080, 0.3)  # 0.0046 refers to 0,5 C; 0,1 for fast computing
    R_unc = ureal(0, 0.000012)
    R_range_unc = R_range + R_unc


    def Temp_res_a7(res, TPW, a, b):
        l = int(len(res))
        Temps = la.ones((1, l))
        for i in range(l):
            W = res[i] / TPW
            dW = (a * (W - 1)) - (b * (W - 1) * log(W))
            WR = W-dW
            Temp = SPRT_1.calculate_temp_from_Wr(WR)
            Temps[0, i] = Temp
        return Temps


    T_calc = Temp_res_a7(R_range_unc, Rtpw, A[0], A[1])

else:
    R_range = np.arange(25.558080,65, 0.1)  # 0.0046 refers to 0,5 C; 0,1 for fast computing
    R_unc = ureal(0, 0.000012)
    R_range_unc = R_range + R_unc


    def Temp_res_a7(res, TPW, a, b):
        l = int(len(res))
        Temps = la.ones((1, l))
        for i in range(l):
            W = res[i] / TPW
            dW =(a * (W - 1)) + (b * (W - 1)**2)
            WR = W-dW
            Temp = SPRT_1.calculate_temp_from_Wr(WR)
            Temps[0, i] = Temp
        return Temps


    T_calc = Temp_res_a7(R_range_unc, Rtpw, A[0], A[1])
    print(A)


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

























