# python ./pandas_dataframe/src/insert.py

import pandas as pd

_dataframe = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})

print('\n')

print(_dataframe)

_dataframe.insert(1, "newcol", [99, 99])

print('\n')

print(_dataframe)

_dataframe.insert(0, "col1", [100, 100], allow_duplicates=True)

print('\n')

print(_dataframe)

_dataframe.insert(0, "col0", pd.Series([5, 6], index=[1, 2]))

print('\n')

print(_dataframe)