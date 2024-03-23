# python ./pandas_dataframe/src/shape.py

import pandas as pd

_dataframe = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})

print('\n')

print(_dataframe.shape)

print('\n')

print(_dataframe)

_dataframe = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4],
                           'col3': [5, 6]})

print('\n')

print(_dataframe.shape)

print('\n')

print(_dataframe)
