i = 0

while \
    i < 5:
        print(i)
        i += 1
i = None

for \
    i in range(5):
        print(i)

for \
    i in [1, 2, 3, 4]:
        print(i)

for \
    c in '''hello''':
        print(c)

for \
    x in ('a', 'b', 'c', 4):
        print(x)

for \
    i, j in [(1, 2), (3, 4), (5, 6)]:
        print(i, j)

for \
    i in range(5):
        if i == 3:
                break
        print(i)

for \
    i in range(1, 8):
        print(i)
        if \
            i % 7 == 0:
                print('''Multiple of 7 found''')
                break
else:
        print('''No multiples o 7 in the range''')

for \
    i in range(5):
        try:
                10 / (i - 3)
        except ZeroDivisionError:
                print('''Divided by 0''')
                continue
        finally:
                print(''''Always run''')
        print(i)

s = '''hello'''

for \
    c in s:
        print(c)

i = 0
for \
    c in s:
        print(i, c)
        i += 1

for \
    i in range(len(s)):
        print(i, s[i])

for \
    i, c in enumerate(s):
        print(i, c)