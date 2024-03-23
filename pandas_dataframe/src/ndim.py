# python ./pandas_dataframe/src/ndim.py

import pandas as pd

import numpy as np

_serie = pd.Series({'a': 1, 'b': 2, 'c': 3})

print('\n')

print(_serie.ndim)

print('\n')

print(_serie)

_dataframe = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})

print('\n')

print(_dataframe.ndim)

print('\n')

print(_dataframe)
