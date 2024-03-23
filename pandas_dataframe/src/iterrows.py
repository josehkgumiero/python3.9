# python ./pandas_dataframe/src/iterrows.py

import pandas as pd

_dataframe = pd.DataFrame([[1, 1.5]], columns=['int', 'float'])

row = next(_dataframe.iterrows())[1]

print(row)

print("\n")

print(row['int'].dtype)

print("\n")

print(_dataframe['int'].dtype)
