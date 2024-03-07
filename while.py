i = 5

while \
    i < 5:
        print(i)
        i += 1

while True:
        print(i)
        if \
            i >= 5:
                break
                print('''something''')

min_length = 2

name = input('''Please enter your name: ''')

while not(
        len(name) >= min_length \
        and name.isprintable() \
        and name.isalpha()
):
        name = input('''Please enter your name: ''')

print(
        '''Hello, {0}'''.format(name)
)

while True:
        name = input('''Please eter your name: ''')
        if len(name) >= min_length \
        and name.isprintable() \
        and name.isalpha():
                break
print('''Hello, {0}'''.format(name))


a = 0
while \
    a < 10:
        a += 1
        if \
            a % 2 == 0:
                continue
        print(a)

l = [
        1,
        2,
        3
]

val = 10

found = False

idx = 0

while \
    idx < len(l):
        if [idx] == val:
                found = True
                break
        idx += 1

if not found:
        l.append(val)

print(l)