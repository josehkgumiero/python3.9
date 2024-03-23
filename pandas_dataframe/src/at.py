# python ./pandas_dataframe/src/at.py

import pandas as pd

_dataframe = pd.DataFrame([[0, 2, 3], [0, 4, 1], [10, 20, 30]],
                          index=[4, 5, 6], columns=['A', 'B', 'C'])

print("\n")

print(_dataframe)

print("\n")

print(_dataframe.at[4, 'B'])

_dataframe.at[4, 'B'] = 10

print("\n")

print(_dataframe.at[4, 'B'])

print("\n")

print(_dataframe.loc[4].at['B'])