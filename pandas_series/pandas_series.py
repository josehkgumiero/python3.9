# pandas.Series

# class pandas.Series(
#   data=None,
#   index=None,
#   dtype=None,
#   name=None,
#   copy=None,
#   fastpath=_NoDefault.no_default
#)

# One-dimensional ndarray with axis labels.
# Labels need to be unique but must be a hashable type.
# The object supports both integer and label-based indexing.
# Provides a host of methods for performing operations involving the index.
# Statistical methods from ndarray have been overridden to automatically exclude missing data.

#Parameters:

#data
#array-like, Iterable, dict, or scalar value
#Contains data stored in Series. If data is a dict, argument order is maintained.

#index
#array-like or Index (1d)
#Values must be hashable and have the same length as data. Non-unique index values are allowed. Will default to RangeIndex (0, 1, 2, …, n) if not provided. If data is dict-like and index is None, then the keys in the data are used as the index. If the index is not None, the resulting Series is reindexed with the index values.

#dtype
#str, numpy.dtype, or ExtensionDtype, optional
#Data type for the output Series. If not specified, this will be inferred from data. See the user guide for more usages.

#name
#Hashable, default None
#The name to give to the Series.

#copy
#bool, default False
#Copy input data. Only affects Series or 1d ndarray input. See examples.

import pandas as pd

_d1 = {
    'a': 1,
    'b': 2,
    'c': 3
}

_ser1 = pd.Series(
    data=_d1,
    index=['a','b','c']
)

print("\n")

print(_ser1)

_d2 = _d1

_ser2 = pd.Series(
    data=_d1,
    index=['x','y','z']
)

print("\n")

print(_ser2)

_l3 = [1, 2]

_ser3 = pd.Series(_l3, copy=False)

_ser3.iloc[0] = 999

print("\n")

print(_l3)

print(_ser3)

_l4 = [1, 2]

_ser4 = pd.Series(_l4, copy=True)

_ser4.iloc[0] = 1000

print("\n")

print(_l4)

print(_ser4)

# pandas.Series.index

# Series.index

# The index (axis labels) of the Series

# The index of a Series is used to label ad identify each eleent of the underlying data.
# The index can be thought of as an immutable ordered set (technically a multi-set, as it may contain duplicate labels),
# and is used to index and align data in pandas

_cities = ['Kolkata', 'Chicago', 'Toronto', 'Lisbon']
_populations = [14.85, 2.71, 2.93, 0.51]
_city_series = pd.Series(_populations, index=_cities)

print("\n")

print(_city_series.index)

_city_series.index = ['KOL', 'CHI', 'TOR', 'LIS']

print("\n")

print(_city_series.index)

print("\n")

print(_city_series)

# pandas.Series.array

# property Series.array

# The ExtensionArray of the data backing this Series or Index

# Returns:

# ExtensionArray

# An ExtensionArray of the values stored within. 
# For extension types, this is the actual array.
# For NumPy native types, this is a thin (no copy) wrapper around numpy.ndarray.
# .array differs from .values, which may require converting the data to a different form.

# dtype                 array type
# category              Categorical
# period                PeriodArray
# interval              IntervalArray
# IntegerNA             IntegerArray
# string                StringArray
# boolean               BooleanArray
# datetime64[ns, tz]    DatetimeArray

_l5 = [1, 2, 3]

print("\n")

print(pd.Series(_l5).array)

_l6 = ['a', 'b', 'c']

print("\n")

print(pd.Series(pd.Categorical(_l6)).array)

# pandas.Series.values

# property Series.values

# Return Series as ndarray or ndarray-like depending on the dtype.

_l7 = [1, 2, 3]

print("\n")

print(pd.Series(_l7).values)

_l8 = list('aabc')

print("\n")

print(pd.Series(_l8).values)

_l9 = _l8

print("\n")

print(pd.Series(_l9).astype('category').values)