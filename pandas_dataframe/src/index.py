# python ./pandas_dataframe/src/index.py

import pandas as pd

_dataframe = pd.DataFrame(
    {
        'Name': ['Alice', 'Bob', 'Aritra'],
        'Age': [25, 30, 35],
        'Location': ['Seattle', 'New York', 'Kona']
    },
    index=([10, 20, 30])
)

print('\n')

print(_dataframe.index)

print('\n')

print(_dataframe)

