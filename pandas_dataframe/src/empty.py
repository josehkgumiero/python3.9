# python ./pandas_dataframe/src/empty.py

import pandas as pd

import numpy as np

_dataframe = pd.DataFrame({'A' : []})

print('\n')

print(_dataframe)

print('\n')

print(_dataframe.empty)

_dataframe = pd.DataFrame({'A' : [np.nan]})

print('\n')

print(_dataframe)

print('\n')

print(_dataframe.dropna().empty)

_serie = pd.Series({'A' : []})

print('\n')

print(_serie)

print('\n')

print(_serie.empty)

_serie = pd.Series()

print('\n')

print(_serie)

print('\n')

print(_serie.empty)