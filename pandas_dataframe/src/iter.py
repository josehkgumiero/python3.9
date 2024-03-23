# python ./pandas_dataframe/src/iter.py

import pandas as pd

_dataframe = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

for _index in _dataframe:
    print(_index)