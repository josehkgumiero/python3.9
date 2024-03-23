# python ./pandas_dataframe/src/values.py

import pandas as pd

import numpy as np

_dataframe = pd.DataFrame({'age':    [3,  29],
                           'height': [94, 170],
                           'weight': [31, 115]})

print('\n')

print(_dataframe)

print('\n')

print(_dataframe.values)

_dataframe = pd.DataFrame([('parrot',   24.0, 'second'),
                           ('lion',     80.5, 1),
                           ('monkey', np.nan, None)],
                          columns=('name', 'max_speed', 'rank'))

print('\n')

print(_dataframe)

print('\n')

print(_dataframe.values)

print('\n')

print(_dataframe.dtypes)
