# python ./pandas_dataframe/src/axes.py

import pandas as pd

import numpy as np

_dataframe = pd.DataFrame({'col1': [1, 2, 3, 4], 'col2': [5, 6, 7, 8], 'col3': [9, 10, 11, 12]})

print('\n')

print(_dataframe)

print('\n')

print(_dataframe.axes)
