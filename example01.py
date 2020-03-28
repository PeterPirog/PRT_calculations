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



if __name__ == "__main__":
    # USING 2d -list, no uncertainties
    print('\n Example - 2D or 1D -list, no uncertainties')
    value_list=[[1,2,3,4],[5,6,7,8]]
    unc_array =urealext(value_list, k=2, array_label='point')
    print('\nvalue_list=', value_list)
    print('\nunc_array=', unc_array)

    print('\nExample - single value, no uncertainties')
    value_list=2
    unc_array =urealext(value_list, k=2, array_label='point')
    print('\nvalue_list=', value_list)
    print('\nunc_array=', unc_array)

    print('\n Example - 2D or 1D -value list, the same uncertainty for all values, k=1')
    value_list=[[1,2,3,4],[5,6,7,8]]
    unc_list=0.1
    unc_array =urealext(value_list,unc_list, k=1, array_label='point')
    print('\nvalue_list=', value_list)
    print('\nunc_array=', unc_array)

    print('\n Example - 2D or 1D -value list, 2D or 1D uncertainty list, k=2, points name - voltage')
    value_list=[[1,2,3,4],[5,6,7,8]]
    unc_list=[[0.1,0.1,0.1,0.1],[0.2,0.2,0.2,0.15]]
    unc_array =urealext(value_list,unc_list, k=2, array_label='voltage')
    print('\nvalue_list=', value_list)
    print('\nunc_array=', unc_array)

    print('\n Calculating sine from uncertainty array')
    print('\n',GTC.sin(unc_array))


    value_list=[[1,2],[5,6]]
    unc_list=[[0.1,0.1],[0.2,0.2]]
    unc_array=urealext(value_list,unc_list)
    print('\n Calculating inverse matrix from uncertainty array')
    print('\n',GTC.la.inv(unc_array))     # <<<<<-------------------  ERROR




