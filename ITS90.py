# GTC ==1.2.0
import GTC
from GTCext import *
import numpy as np
import pandas as pd

# ITS-90 functionc  calculated  according to "Guide to the realization of the ITS-90", platinum resistance termometry
# import numpy as np
import GTC
import math


def conv_celsius2kelvin(temp_c):
    return float2GTC(temp_c) + 273.15


def conv_kelvin2celsius(temp_k):
    return float2GTC(temp_k) - 273.15


def calculate_Wr_unc(temp_C, verbose=False):
    """
    Function calculate reference function Wr for temperature t with uncertainty as a urealtype
    :param temp_C:
    :param verbose:
    :return:
    """
    # constants for temperature range -259.3467 C to 0 C
    A = [-2.13534729,  # A0
         3.18324720,  # A1
         -1.80143597,  # A2
         0.71727204,  # A3
         0.50344027,  # A4
         -0.61899395,  # A5
         -0.05332322,  # A6
         0.28021362,  # A7
         0.10715224,  # A8
         -0.29302865,  # A9
         0.04459872,  # A10
         0.11868632,  # A11
         -0.05248134]  # A12
    # constants for temperature range 0 C to 961.78 C
    C = [2.78157254,  # C0
         1.64650916,  # C1
         -0.13714390,  # C2
         -0.00649767,  # C3
         -0.00234444,  # C4
         0.00511868,  # C5
         0.00187982,  # C6
         -0.00204472,  # C7
         -0.00046122,  # C8
         0.00045724]  # C9
    temp_C = float2GTC(temp_C)
    temp_K = conv_celsius2kelvin(temp_C)
    Wr = 1
    if (temp_C.x >= -259.3467) and (temp_C.x < 0):
        for i in range(13):
            if i == 0:
                sum = A[0]
            else:
                sum = sum + A[i] * GTC.pow((GTC.log(temp_K / 273.16) + 1.5) / 1.5, i)
        Wr = GTC.exp(sum)
    elif (temp_C.x >= 0) and (temp_C.x <= 961.78):
        for i in range(10):
            if i == 0:
                sum = C[0]
            else:

                sum = sum + C[i] * GTC.pow((temp_K - 754.15) / 481, i)
        Wr = sum
    else:
        print("temperature out of range")
    if verbose:
        print("Wr({}, unc std:{})={}, unc std:{}".format(temp_C.x, temp_C.u, Wr.x, Wr.u))
    return Wr
def calculate_Wr(temp_C, verbose=False):
    """
    Function calculate reference function Wr for temperature t as numpy
    :param temp_C:
    :param verbose:
    :return:
    """
    # constants for temperature range -259.3467 C to 0 C
    A = [-2.13534729,  # A0
         3.18324720,  # A1
         -1.80143597,  # A2
         0.71727204,  # A3
         0.50344027,  # A4
         -0.61899395,  # A5
         -0.05332322,  # A6
         0.28021362,  # A7
         0.10715224,  # A8
         -0.29302865,  # A9
         0.04459872,  # A10
         0.11868632,  # A11
         -0.05248134]  # A12
    # constants for temperature range 0 C to 961.78 C
    C = [2.78157254,  # C0
         1.64650916,  # C1
         -0.13714390,  # C2
         -0.00649767,  # C3
         -0.00234444,  # C4
         0.00511868,  # C5
         0.00187982,  # C6
         -0.00204472,  # C7
         -0.00046122,  # C8
         0.00045724]  # C9
    temp_K = temp_C+ 273.15
    Wr = 1
    if (temp_C >= -259.3467) and (temp_C < 0):
        for i in range(13):
            if i == 0:
                sum = A[0]
            else:
                sum = sum + A[i] * pow((math.log(temp_K / 273.16) + 1.5) / 1.5, i)
        Wr = GTC.exp(sum)
    elif (temp_C>= 0) and (temp_C<= 961.78):
        for i in range(10):
            if i == 0:
                sum = C[0]
            else:

                sum = sum + C[i] * pow((temp_K - 754.15) / 481, i)
        Wr = sum
    else:
        print("temperature out of range")
    if verbose:
        print("Wr({}, unc std:{})={}, unc std:{}".format(temp_C.x, temp_C.u, Wr.x, Wr.u))
    return Wr

def calculate_temp_from_Wr_unc(W, verbose=False):
    W = float2GTC(W)
    # constants for temperature  calculation range -259.3467 C to 0 C
    B = [0.183324722,  # B0
         0.240975303,  # B1
         0.209108771,  # B2
         0.190439972,  # B3
         0.142648498,  # B4
         0.077993465,  # B5
         0.012475611,  # B6
         -0.032267127,  # B7
         -0.075291522,  # B8
         -0.056470670,  # B9
         0.076201285,  # B10
         0.123893204,  # B11
         -0.029201193,  # B12
         -0.091173542,  # B13
         0.001317696,  # B14
         0.026025526]  # B15
    # constants for temperature calculation range 0 C to 961.78 C
    D = [439.932854,  # D0
         472.418020,  # D1
         37.684494,  # D2
         7.472018,  # D3
         2.920828,  # D4
         0.005184,  # D5
         -0.963864,  # D6
         -0.188732,  # D7
         0.191203,  # D8
         0.049025]  # D9
    temp_k = 0
    if W.x <= 1:
        for i in range(16):
            if i == 0:
                sum = B[0]
            else:
                sum = sum + B[i] * GTC.pow((GTC.pow(W, 1 / 6) - 0.65) / 0.35, i)
        temp_k = 273.16 * sum
    else:
        for i in range(10):
            if i == 0:
                sum = 0
            else:
                sum = sum + D[i] * GTC.pow((W - 2.64) / 1.64, i)
        temp_k = 273.15 + D[0] + sum
    temp_C = conv_kelvin2celsius(temp_k)
    if verbose:
        # print("W({})={}".format(temp_c, W))
        print("T({}, unc std:{})={}, unc std:{}".format(W.x, W.u, temp_C.x, temp_C.u))
    return temp_C
def calculate_temp_from_Wr(W):
    # constants for temperature  calculation range -259.3467 C to 0 C
    B = [0.183324722,  # B0
         0.240975303,  # B1
         0.209108771,  # B2
         0.190439972,  # B3
         0.142648498,  # B4
         0.077993465,  # B5
         0.012475611,  # B6
         -0.032267127,  # B7
         -0.075291522,  # B8
         -0.056470670,  # B9
         0.076201285,  # B10
         0.123893204,  # B11
         -0.029201193,  # B12
         -0.091173542,  # B13
         0.001317696,  # B14
         0.026025526]  # B15
    # constants for temperature calculation range 0 C to 961.78 C
    D = [439.932854,  # D0
         472.418020,  # D1
         37.684494,  # D2
         7.472018,  # D3
         2.920828,  # D4
         0.005184,  # D5
         -0.963864,  # D6
         -0.188732,  # D7
         0.191203,  # D8
         0.049025]  # D9
    temp_k = 0
    if W<= 1:
        for i in range(16):
            if i == 0:
                sum = B[0]
            else:
                sum = sum + B[i] * pow((pow(W, 1 / 6) - 0.65) / 0.35, i)
        temp_k = 273.16 * sum
    else:
        for i in range(10):
            if i == 0:
                sum = 0
            else:
                sum = sum + D[i] * pow((W - 2.64) / 1.64, i)
        temp_k = 273.15 + D[0] + sum
    temp_C = temp_k- 273.15
    return temp_C
def create_Wt1_array(Wt,range=7):
    """
    Function to create W(t)-1, array to prepare equation system for solving
    equation system has form Ax coeff=B, function creates matrix A for proper ITS range, default range is 7, for 0C to 660 C
    :param Wt:
    :param range:
    :return:
    """
    if range==7:
        Wt1 = np.reshape(Wt - 1, (-1, 1))
        Wt1_pow2=np.reshape(Wt1**2,(-1,1))
        Wt1_pow3 = np.reshape(Wt1 ** 3, (-1, 1))
        Wt1_array = np.hstack((Wt1, Wt1_pow2, Wt1_pow3))
    return Wt1_array
def create_Wt1_array_unc(Wt,range=7):
    """
    Function to create W(t)-1, array to prepare equation system for solving
    equation system has form Ax coeff=B, function creates matrix A for proper ITS range, default range is 7, for 0C to 660 C
    :param Wt:
    :param range:
    :return:
    """
    if range==7:
        Wt1 = np.reshape(Wt - 1, (-1, 1))
        Wt1_pow2=np.reshape(Wt1**2,(-1,1))
        Wt1_pow3 = np.reshape(Wt1 ** 3, (-1, 1))
        Wt1_array = np.hstack((Wt1, Wt1_pow2, Wt1_pow3))
    return Wt1_array


class PRT():
    def __init__(self, model=None, numer=None, nazwa_pliku_xls='Dane_termometrow.xlsx'):
        self.model = model
        self.numer = numer
        self.plik_danych = nazwa_pliku_xls
        self.__wczytaj_dane_sondy()
        # self.Wt=np.array([])
        # self.R0 = ureal()

    def __odczyt2wektor(self, odczyt, niepewnosc_rozszerzona=0):
        return 1

    def __wczytaj_dane_sondy(self):
        self.data = pd.read_excel(io=self.plik_danych, sheet_name=self.model + '_' + self.numer)
        # print(self.data)

    def metoda1(self):
        print("model to", self.model)
        print("numer to", self.numer)
