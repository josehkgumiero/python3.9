# python ./pandas_dataframe/src/set_flags.py

import pandas as pd

import numpy as np

_dataframe = pd.DataFrame({"A": [1, 2]})

print('\n')

print(_dataframe.flags.allows_duplicate_labels)

_dataframe2 = _dataframe.set_flags(allows_duplicate_labels=False)

print('\n')

print(_dataframe2.flags.allows_duplicate_labels)
