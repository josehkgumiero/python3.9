# python ./pandas_dataframe/src/memory_usage.py

import pandas as pd

import numpy as np

dtypes = ['int64', 'float64', 'complex128', 'object', 'bool']

_data = dict([(t, np.ones(shape=5000, dtype=int).astype(t))
             for t in dtypes])

_dataframe = pd.DataFrame(_data)

print('\n')

print(_dataframe.head())

print('\n')

print(_dataframe.memory_usage())

print('\n')

print(_dataframe.memory_usage(index=False))

print('\n')

print(_dataframe.memory_usage(deep=True))