# python ./pandas_dataframe/src/bool.py

import pandas as pd

_serie = pd.Series([True]).bool()

print("\n")

print(_serie)

_serie = pd.Series([False]).bool()  

print("\n")

print(_serie)

_dataframe = pd.DataFrame({'col': [True]}).bool()  

print("\n")

print(_dataframe)

_dataframe = pd.DataFrame({'col': [False]}).bool()  

print("\n")

print(_dataframe)