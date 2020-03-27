import numpy as np
import ITS90 as SPRT_1
from scipy.interpolate import lagrange
from numpy.polynomial.polynomial import Polynomial
########################### Dane cwiczebne
T1=231.928
T2=419.527
T3=660.323
T4=961.780

Rtpw=2.5534637
uRtpw=0.0000041

uT1=0.0015
uT2=0.0017
uT3=0.0040
uT4=0.0052


WSn=1.89259628
WZn=2.56855103
WAl=3.37543469
WAg=4.28556295

Wr_Sn=SPRT_1.Calculate_Wr(T1)
Wr_Zn=SPRT_1.Calculate_Wr(T2)
Wr_Al=SPRT_1.Calculate_Wr(T3)
Wr_Ag=SPRT_1.Calculate_Wr(T4)

#Wr_Sn=1.89279768
#Wr_Zn=2.56891730
#Wr_Al=3.37600860
#Wr_Ag=4.28642053
#########################
WFP_array=np.array([[WSn],[WZn],[WAl]])
Wr_array=np.array([[Wr_Sn],[Wr_Zn],[Wr_Al]])


M_array=np.array([[WSn-1,(WSn-1)**2,(WSn-1)**3],[WZn-1,(WZn-1)**2,(WZn-1)**3],[WAl-1,(WAl-1)**2,(WAl-1)**3]])
Y_array=Wr_array-WFP_array

M_inv=np.linalg.inv(M_array)
A=np.matmul(M_inv,Y_array)
print(M_array)
print(A)











