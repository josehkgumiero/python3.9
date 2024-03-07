def f1(a, b, c):
    print(
        '''
        a = {0}, b = {1}, c = {2}
        ''' \
        .format(a, b, c)
    )

f1(1, 2, 3)

f1(1, 2)

def f2(a, b = 2, c = 3):
    print(
        '''
        a = {0}, b = {1}, c = {2}
        ''' \
        .format(a, b, c)
    )

f2(10, 20, 30)

f2(10, 20)

f2(10)

f2()