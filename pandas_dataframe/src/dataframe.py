# python ./pandas_dataframe/src/dataframe.py

from dataclasses import make_dataclass
import pandas as pd

import numpy as np

_data = {
    'col1': [1, 2],
    'col2': [3, 4]
}


# Constructing FataFrame from a dictionary.

_dataframe = pd.DataFrame(data=_data)

print('\n')

print(_dataframe)


# Notice that the inferred dtype is int64.

print('\n')

print(_dataframe.dtypes)


# to enforce a single dtype

_dataframe = pd.DataFrame(data=_data, dtype=np.int8)

print('\n')

print(_dataframe.dtypes)


# Constructing DataFrame from a dictionary including Series:

_data = {
    'col1': [0, 1, 2, 3],
    'col2': pd.Series([2, 3], index=[2, 3])
}

_dataframe = pd.DataFrame(data=_data, index=[0, 1, 2, 3])

print('\n')

print(_dataframe)


# Constructing DataFrame from numpy ndarray:

_dataframe = pd.DataFrame(np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]),
    columns=['a', 'b', 'c']
)

print('\n')

print(_dataframe)


# Constructing DataFrame from a numpy ndarray that has labeled columns:

_data = np.array(
    [
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9)
    ],
    dtype=[
        ("a", "i4"),
        ("b", "i4"),
        ("c", "i4")
    ]
)

_dataframe = pd.DataFrame(_data, columns=["c", "a"])

print('\n')

print(_dataframe)


# Constructing DataFrame from dataclass:

Point = make_dataclass("Point", [("x", int), ("y", int)])

_dataframe = pd.DataFrame([Point(0, 0), Point(0, 3), Point(2, 3)])

print('\n')

print(_dataframe)


# Constructing DataFrame from Series/DataFrame:

_data = pd.Series([1, 2, 3], index=["a", "b", "c"])

_dataframe = pd.DataFrame(data=_data, index=["a", "c"])

print('\n')

print(_dataframe)


_data = pd.DataFrame([1, 2, 3], index=["a", "b", "c"], columns=["x"])

_dataframe = pd.DataFrame(data=_data, index=["a", "c"])

print('\n')

print(_dataframe)
