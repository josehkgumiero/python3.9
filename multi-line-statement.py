a = [1, 2, 3]

print(a)

b = [ 
    1, 
    2,
    2,
    4,
    5    
]

print(b)

c = (
    1,
    2,
    3
)

print(c)

d = {
    "key1": 1,
    "key2": 2
}

print(d)

def e_func(
        f,
        g,
        h,
        i
):
    print(
        f,
        g,
        h,
        i
    )

e_func(10, 20, 30, 40)

j = 10
k = 20
l = 30
m = 40

if \
    j > 5 \
       and k > 10 \
            and l > 20 \
                and m > 30:
    print(True)

n = '''This is a String'''

print(n)

o = '''
    This
    other
    String
'''

print(o)

p = '''
    some items:
    1. item 1
    2. item 2
'''

print(p)

def q_func():
    q = '''
        a multi-line string
        that is indented in
        the second line
        '''
    return q

print(q_func())