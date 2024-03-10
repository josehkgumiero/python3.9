# Sequence Type Mutable

l = [1, 2, 3, 4, 5]

print(id(l))

print(l[0])

l[0] = 'a'

print(l)

print(id(l))

l.clear()

print(l)

l = [1, 2, 3, 4, 5]

print(id(l), l)

l = []

print(l)

print(id(l))

suits = ['spades', 'hearts', 'diamons', 'clubs']

alias = suits

print(id(alias), id(suits))

alias.clear()

print(alias)

print(suits)

suits = ['spades', 'hearts', 'diamons', 'clubs']

def something(l):
    l.clear()

something(suits)

print(suits)

l = [1, 2, 3]

print(id(l))

l = l + [4]

print(id(l))

l.clear()

l = [1, 2, 3]

print(id(l))

l.append(4)

print(id(l))

l.clear()

l = [1, 2, 3]

print(l)

print(id(l))

l.extend([4])

print(l)

l.extend(['a','b','c'])

print(id(l))

