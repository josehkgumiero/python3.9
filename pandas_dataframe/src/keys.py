# python ./pandas_dataframe/src/keys.py

import pandas as pd

_dataframe = pd.DataFrame(data={'A': [1, 2, 3], 'B': [0, 4, 8]},
                 index=['a', 'b', 'c'])

print("\n")

print(_dataframe)

print("\n")

print(_dataframe.keys())
