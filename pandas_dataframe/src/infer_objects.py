# python ./pandas_dataframe/src/infer_objects.py

import pandas as pd


_dataframe = pd.DataFrame({"A": ["a", 1, 2, 3]})

print('\n')

print(_dataframe)

_dataframe = _dataframe.iloc[1:]

print(_dataframe.dtypes)

print(_dataframe.infer_objects().dtypes)