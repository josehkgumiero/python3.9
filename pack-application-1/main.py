import common.validators.boolean

import common.validators.json

import common.validators.numeric

common.validators.json.is_json('{}')

date = '2018-01-01'

common.validators.numeric.is_numeric(10)

common.validators.numeric.is_integer('100')

print('\n\n***** self *****')

for k in dict(globals()).keys():
    print(k)

print('\n\n***** common *****')

for k in common.__dict__.keys():
    print(k)

print('\n\n***** validator *****')

for k in common.validators.__dict__.keys():
    print(k)
