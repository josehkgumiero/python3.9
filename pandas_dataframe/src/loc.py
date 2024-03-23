# python ./pandas_dataframe/src/loc.py

import pandas as pd

_dataframe = pd.DataFrame([[1, 2], [4, 5], [7, 8]],
                          index=['cobra', 'viper', 'sidewinder'],
                          columns=['max_speed', 'shield'])

print("\n")

print(_dataframe)

print("\n")

print(_dataframe.loc['viper'])

print("\n")

print(_dataframe.loc[['viper', 'sidewinder']])

print("\n")

print(_dataframe.loc['cobra', 'shield'])

print("\n")

print(_dataframe.loc['cobra':'viper', 'max_speed'])

print("\n")

print(_dataframe.loc[[False, False, True]])

print("\n")

print(_dataframe.loc[pd.Series([False, True, False],
                               index=['viper', 'sidewinder', 'cobra'])])

print("\n")

print(_dataframe.loc[pd.Index(["cobra", "viper"], name="foo")])

print("\n")

print(_dataframe.loc[_dataframe['shield'] > 6])

print("\n")

print(_dataframe.loc[_dataframe['shield'] > 6, ['max_speed']])

print("\n")

print(_dataframe.loc[(_dataframe['max_speed'] > 1)
      & (_dataframe['shield'] < 8)])

print("\n")

print(_dataframe.loc[(_dataframe['max_speed'] > 4)
      | (_dataframe['shield'] < 5)])

print("\n")

print(_dataframe.loc[lambda _dataframe: _dataframe['shield'] == 8])

_dataframe.loc[['viper', 'sidewinder'], ['shield']] = 50

print("\n")

print(_dataframe)

_dataframe.loc['cobra'] = 10

print("\n")

print(_dataframe)

_dataframe.loc[:, 'max_speed'] = 30

print("\n")

print(_dataframe)

_dataframe.loc[_dataframe['shield'] > 35] = 0

print("\n")

print(_dataframe)

_dataframe.loc["viper", "shield"] += 5

print("\n")

print(_dataframe)

shuffled_df = _dataframe.loc[["viper", "cobra", "sidewinder"]]

_dataframe.loc[:] += shuffled_df

print("\n")

print(_dataframe)

_dataframe = pd.DataFrame([[1, 2], [4, 5], [7, 8]],
                          index=[7, 8, 9], columns=['max_speed', 'shield'])

print("\n")

print(_dataframe)

print("\n")

print(_dataframe.loc[7:9])

tuples = [
    ('cobra', 'mark i'), ('cobra', 'mark ii'),
    ('sidewinder', 'mark i'), ('sidewinder', 'mark ii'),
    ('viper', 'mark ii'), ('viper', 'mark iii')
]

index = pd.MultiIndex.from_tuples(tuples)

values = [[12, 2], [0, 4], [10, 20],
          [1, 4], [7, 1], [16, 36]]

_dataframe = pd.DataFrame(values, columns=['max_speed', 'shield'], index=index)

print("\n")

print(_dataframe)

print("\n")

print(_dataframe.loc['cobra'])

print("\n")

print(_dataframe.loc[('cobra', 'mark ii')])

print("\n")

print(_dataframe.loc['cobra', 'mark i'])

print("\n")

print(_dataframe.loc[[('cobra', 'mark ii')]])

print("\n")

print(_dataframe.loc[('cobra', 'mark i'):'viper'])

print("\n")

print(_dataframe.loc[('cobra', 'mark i'):('viper', 'mark ii')])