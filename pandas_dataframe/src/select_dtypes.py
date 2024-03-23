# python ./pandas_dataframe/src/select_dtypes.py

import pandas as pd

_dataframe = pd.DataFrame({'a': [1, 2] * 3,
                           'b': [True, False] * 3,
                           'c': [1.0, 2.0] * 3})

print('\n')

print(_dataframe.select_dtypes(include='bool'))

print('\n')

print(_dataframe.select_dtypes(include='float64'))

print('\n')

print(_dataframe.select_dtypes(include='int64'))

print('\n')

print(_dataframe)
