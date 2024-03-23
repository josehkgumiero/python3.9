# python ./pandas_dataframe/src/items.py

import pandas as pd

_dataframe = pd.DataFrame({'species': ['bear', 'bear', 'marsupial'],
                           'population': [1864, 22000, 80000]},
                          index=['panda', 'polar', 'koala'])

print("\n")

print(_dataframe)

print("\n")

for label, content in _dataframe.items():
    print(f'label: {label}')
    print(f'content: {content}', sep='\n')
