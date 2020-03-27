import GTC
import numpy as np
import pandas as pd


def urealext(value_list, unc_list=0.0, k=2, array_label='X', df=GTC.inf):
    # INPUT variables:
    # for value_list are:
    #       <class 'list'>
    #       <class 'numpy.ndarray'>
    #       <class 'int'>
    #       <class 'float'>
    # for unc_list are:
    #       <class 'list'>
    #       <class 'numpy.ndarray'>
    #       <class 'int'>
    #       <class 'float'>
    # for k are:
    #       <class 'int'>
    #       <class 'float'>
    # for value_name are:
    #       <class 'string'>

    if isinstance(value_list, int) or isinstance(value_list, float):  # check if list is single value
        value_list = [[value_list]]
        n_rows = 1
        n_cols = 1
    else:
        # find size of value_list
        n_rows = len(value_list)
        n_cols = len(value_list[0])

    if df == 'N':
        df = n_rows * n_cols - 1

    realnumber_list = [[0 for x in range(n_cols)] for x in range(n_rows)]

    for i in range(n_rows):
        for j in range(n_cols):
            label = array_label + str(i) + '_' + str(j)
            if isinstance(unc_list, int) or isinstance(unc_list, float):
                unc_std = unc_list / k
            else:
                unc_std = unc_list[i][j] / k
            realnumber_list[i][j] = GTC.ureal(x=value_list[i][j], u=unc_std, label=label, df=df)
    unc_array = GTC.la.uarray(realnumber_list)

    return unc_array


def isGTC(value):
    typeGTC = type(GTC.ureal(0, 0))
    if type(value) == typeGTC:
        return True
    else:
        return False


# converting float type to GTC uncertainty type
def float2GTC(value):
    if isGTC(value):
        return value
    else:
        return GTC.ureal(value, 0)

def pinv(uncertainty_array):
    return uncertainty_array
