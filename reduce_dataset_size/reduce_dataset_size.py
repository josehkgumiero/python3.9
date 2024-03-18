import os
import pandas as pd
import numpy as np

_list = []

for root, dirs, files in os.walk('.'):
    _tuple = (root, dirs, files)
    _list.append(_tuple)

_data = np.array(_list, dtype=object)

_df = pd.DataFrame.from_records(_data)

_df = _df.rename(columns={0: 'Root', 1: 'Directory', 2: 'File'})

_file_serie = _df['File']

_check_list_dataset = ["1800.csv", "fakefriends.csv", "u.data"]

def _str_contains(_list_object):
    _list_dataset_founded = []
    for _dataset in _check_list_dataset:
        if _dataset in _list_object:
            _list_dataset_founded.append(_dataset)
    return _list_dataset_founded

_file_serie = _file_serie.apply(_str_contains)

_values = _file_serie.values

unique, counts = np.unique(_values, return_counts=True)

_list_dataset = []

def _set_dataset(_list):
    for _index in range(0, len(_list)):
        if isinstance(_list[_index], list):
            _set_dataset(_list[_index])
        else:
            _list_dataset.append(_list[_index])

_set_dataset(unique)

print(_list_dataset)