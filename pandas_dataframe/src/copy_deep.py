# python ./pandas_dataframe/src/copy_deep.py

import pandas as pd

_serie = pd.Series([1, 2], index=["a", "b"])

print('\n')

print(_serie)

_otherSerie = _serie.copy()

print('\n')

print(_otherSerie)

_shallowCopySerie = _serie.copy(deep=False)

print('\n')

print(_shallowCopySerie)

print('\n')

print(_serie is _shallowCopySerie)

print('\n')

print(_serie.values is _shallowCopySerie.values and _serie.index is _shallowCopySerie.index)

_deepCopySerie = _serie.copy(deep=True)

print('\n')

print(_serie is _deepCopySerie)

print('\n')

print(_serie.values is _deepCopySerie.values and _serie.index is _deepCopySerie.index)

_serie.iloc[0] = 3

_shallowCopySerie.iloc[1] = 4

print(_serie)

print(_shallowCopySerie)

print(_deepCopySerie)