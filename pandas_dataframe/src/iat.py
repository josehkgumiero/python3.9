# python ./pandas_dataframe/src/iat.py

import pandas as pd

_dataframe = pd.DataFrame([[0, 2, 3], [0, 4, 1], [10, 20, 30]],
                          columns=['A', 'B', 'C'])

print("\n")

print(_dataframe)

print("\n")

print(_dataframe.iat[1, 2])

_dataframe.iat[1, 2] = 10

print("\n")

print(_dataframe.iat[1, 2])

print("\n")

print(_dataframe.loc[1].iat[2])