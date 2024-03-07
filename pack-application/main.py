import pack.pack_1

print(pack.pack_1.value)

print('pack_1' in globals())

import sys

print('pack_1' in sys.modules)

print('pack.pack_1' in sys.modules)

print('pack.pack_1' in globals())

print(
    id(pack.pack_1) == sys.modules['pack.pack_1']
)

print(
    id(pack.pack_1)
)

print(
    id(sys.modules['pack.pack_1'])
)