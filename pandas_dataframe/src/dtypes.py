# python ./pandas_dataframe/src/dtypes.py

import pandas as pd

_dataframe = pd.DataFrame({'float': [1.0],
                           'int': [1],
                           'datetime': [pd.Timestamp('20180310')],
                           'string': ['foo']})

print('\n')

print(_dataframe.dtypes)

print('\n')

print(_dataframe)
