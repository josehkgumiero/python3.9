# python ./pandas_dataframe/src/iterrows.py

import pandas as pd

_dataframe = pd.DataFrame({'num_legs': [4, 2], 'num_wings': [0, 2]},
                          index=['dog', 'hawk'])

print("\n")

print(_dataframe)

for row in _dataframe.itertuples():
    print(row)
