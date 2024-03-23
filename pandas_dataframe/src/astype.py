# python ./pandas_dataframe/src/astype.py

import pandas as pd

import numpy as np

_data = {'col1': [1, 2], 'col2': [3, 4]}

_dataframe = pd.DataFrame(data=_data)

print('\n')

print(_dataframe.dtypes)

print('\n')

print(_dataframe.astype('int32').dtypes)

print('\n')

print(_dataframe.astype({'col1': 'int32'}).dtypes)

print('\n')

print(_dataframe.dtypes)

_serie = pd.Series([1, 2], dtype='int32')

print('\n')

print(_serie)

print('\n')

print(_serie.astype('int64'))

print('\n')

print(_serie)

print('\n')

print(_serie.astype('category'))


# Convert to ordered categorical type with custom ordering:

from pandas.api.types import CategoricalDtype
cat_dtype = CategoricalDtype(
    categories=[2, 1], ordered=True)

print('\n')

print(_serie.astype(cat_dtype))

# Create a series of dates:

_serie_data = pd.Series(pd.date_range('20200101', periods=3))

print('\n')

print(_serie_data)