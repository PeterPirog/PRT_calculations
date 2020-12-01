import GTC
import numpy as np
import pandas as pd

def inv(a): #this function is added cause of error in original linear algebra file
    b = np.identity(a.shape[0], a.dtype)
    return GTC.LU.invab(a, b)

def python_list_transposition(list_2D):
    np_list=np.array(list_2D)
    return np.transpose(np_list).tolist()

def convert_value_to_2Dlist(value):
    if isinstance(value, int) or isinstance(value, float):  # check if list is single value
        value = [[value]]
    else:
        # find size of value_list
        try:
            len(value[0])
        except: # if list is 1D convert to 2D
            value = [value]
    return value

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
    value_list=convert_value_to_2Dlist(value_list)
    unc_list2D =convert_value_to_2Dlist(unc_list)

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
                unc_std = unc_list2D[i][j] / k
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

def calculate_func_from_UncertainArray(function_name, uncertain_array):
    """
    :param function_name:  name of function to calculate form ureal type argument
    :param uncertain_array: array built from UrealArray type
    :return: values of function calculated for each UrealArray element
    """

    n_rows = len(uncertain_array)
    n_cols = len(uncertain_array[0])
    output_array = [[0 for x in range(n_cols)] for x in range(n_rows)]
    for i in range(n_rows):
        for j in range(n_cols):
            output_array[i][j] = function_name(uncertain_array[i][j])
    return output_array

def pinv(GTC_array):
    # A+=(AtxA)^1 x At
    A=GTC_array
    At = GTC.la.transpose(A)
    AtA = GTC.la.matmul(At, A)
    invAtA = inv(AtA)   #corrected version of GTC inv
    pinvA = GTC.la.matmul(invAtA, At)
    return pinvA

def psolve(A,B):
    pinvA=pinv(A)
    result=GTC.la.matmul(pinvA,B)
    return result