a = 10

b = 0

try:
    a / b
except ZeroDivisionError:
    print(
        '''Division by 0'''
    )
finally:
    print(
        '''THis aways executes'''
    )

a = 0

b = 2

while \
    a < 4:
    a += 1
    b -= 1

    try:
        a / b
    except ZeroDivisionError:
        print(
            '''{0}, {1} - division by 0'''.format(a, b)
        )
        continue
    finally:
        print(
            '''{0}, {1}'''.format(a, b)
        )

    print(
        '''{0}, {1} - main loop'''.format(a, b)
    )
else:
    print(
        '''Code executed without a zero division error'''
    )