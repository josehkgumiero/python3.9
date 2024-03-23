# python ./pandas_dataframe/src/convert_dtypes.py

import pandas as pd

import numpy as np

_dataframe = pd.DataFrame(
    {
        "a": pd.Series([1, 2, 3], dtype=np.dtype("int32")),
        "b": pd.Series(["x", "y", "z"], dtype=np.dtype("O")),
        "c": pd.Series([True, False, np.nan], dtype=np.dtype("O")),
        "d": pd.Series(["h", "i", np.nan], dtype=np.dtype("O")),
        "e": pd.Series([10, np.nan, 20], dtype=np.dtype("float")),
        "f": pd.Series([np.nan, 100.5, 200], dtype=np.dtype("float")),
    }
)

print('\n')

print(_dataframe)

print('\n')

print(_dataframe.dtypes)

_otherDataFrame = _dataframe.convert_dtypes()

print('\n')

print(_otherDataFrame)

print('\n')

print(_dataframe.dtypes)


# Start with a Series of strings and missing data represented by np.nan

_serie = pd.Series(["a", "b", np.nan])

print('\n')

print(_serie)

print('\n')

print(_serie.dtypes)

_otherSerie = _serie.convert_dtypes()

print('\n')

print(_otherSerie)

print('\n')

print(_otherSerie.dtypes)
