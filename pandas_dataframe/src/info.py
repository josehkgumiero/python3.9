# python ./pandas_dataframe/src/info.py

import pandas as pd

import numpy as np

int_values = [1, 2, 3, 4, 5]
text_values = ['alpha', 'beta', 'gamma', 'delta', 'epsilon']
float_values = [0.0, 0.25, 0.5, 0.75, 1.0]

_dataframe = pd.DataFrame({"int_col": int_values, "text_col": text_values,
                           "float_col": float_values})

print('\n')

print(_dataframe.info(verbose=True))

print('\n')

print(_dataframe.info(verbose=False))

print('\n')

print(_dataframe)


# Pipe output of DataFrame.info to buffer instead of sys.stdout, get buffer content and writes to a text file:

import io

buffer = io.StringIO()

_dataframe.info(buf=buffer)

s = buffer.getvalue()

with open("./pandas_dataframe/output/_dataframe_info.txt", "w", encoding="utf-8") as f:  
    f.write(s)


# The memory_usage parameter allows deep introspection mode, specially useful for big DataFrames and fine-tune memory optimization:

_dataframe = pd.DataFrame({
    'column_1': np.random.choice(['a', 'b', 'c'], 10 ** 6),
    'column_2': np.random.choice(['a', 'b', 'c'], 10 ** 6),
    'column_3': np.random.choice(['a', 'b', 'c'], 10 ** 6)
})

print('\n')

print(_dataframe.info())

print('\n')

print(_dataframe.info(memory_usage='deep'))

