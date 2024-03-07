from decimal \
    import Decimal

a = 10

b = 3

print(
    a // b,
    a % b 
)

print(
    divmod(
        a,
        b
    )
)

print(
    a == b * ( a // b ) + ( a % b )
)

# help(Decimal)

c = Decimal(-10)

d = Decimal(3)

print(
    c // d,
    c % d 
)

print(
    divmod(
        c,
        d
    )
)

print(
    c == d * ( c // d ) + ( c % d )
)

e = Decimal('0.1')

print(
    e. \
    ln()
)

print(
    e \
    .exp()   
)

print(
    e \
    .sqrt()   
)

