# python ./pandas_dataframe/src/head.py

import pandas as pd

_dataframe = pd.DataFrame({'animal': ['alligator', 'bee', 'falcon', 'lion',
                                  'monkey', 'parrot', 'shark', 'whale', 'zebra']})

print("\n")

print(_dataframe)

print("\n")

print(_dataframe.head())

print("\n")

print(_dataframe.head(3))

print("\n")

print(_dataframe.head(-3))