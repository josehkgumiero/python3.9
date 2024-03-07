txt = """
For only {price:.2f} dollars!
"""
print(txt.format(price = 49))

print("""
My name is {fname}, I am {age}
""".format(fname = "John", age = 36)
)

txt2 = """
My name is {0}, I am {1}
""".format("JOhn", 36)

print(txt2)

txt3 = """
My name is {}, I am {}
""".format("John", 36)

print(txt3)

print("""We have {:<10} chickens.""".format(50))

print("""We have {:>10} chickens.""".format(50))

print("""We have {:^10} chickens.""".format(50))

print("""The temoerature is {:=8} degrees celsius""".format(-5))

print("""The temperature is between {:+} and {:+} degrees celsius""".format(-3, 7))

print("""The temperature is between {:-} and {:-} degrees celsius""".format(-3, 7))

print("""The temperature is between {: } and {: } degrees celsius""".format(-3, 7))

print("""The universe is {:,} years old""".format(13800000000))

print("""The universe is {:_} years old""".format(13800000000))

print("""The binary version of {0} is {0:b}""".format(5))

print("""We have {:d} chickens.""".format(0b101))

print("""We have {:e} chickens.""".format(5))

print("""We have {:E} chickens.""".format(5))

print("""The price is {:.2f} dollars.""".format(45))

x = float('inf')
print("""The price is {:F} dollars.""".format(x))

print("""The price is {:f} dollars.""".format(x))

print("""The octal version of {0} is {0:o}""".format(10))

print("""The Hexadecimal version of {0} is {0:x}""".format(255))

print("""The Hexadecimal version of {0} is {0:X}""".format(255))

print("""You scored {:%}""".format(0.25))

# string literal
year = 2016
event = """Referendum"""
print(f""" Results of the {year} {event} """)

yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)
print("""{:-9} YES votes {:2.2%}""".format(yes_votes, percentage))

s = """Hello World"""
print(str(s))
print(repr(s))
print(str(1/7))

x = 10 * 3.25

y = 200 * 200

print(""""The value of x is {0}, and y is {1} ...""".format(repr(x), repr(y)))

import math
print(f"""THe value of PI is approximately {math.pi:.3f}.""")

table = {'Sjoerd': 4217, 'Jack': 4098, 'DCAB': 7678}
for name, phone in table.items():
    print(f"""{name:10} ===> {phone:10d}""")

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print(
    'Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d};'
    .format(**table)
    )

for x in range(1, 11):
    print("""{0:2d} {1:3d} {2:4d}""".format(x, x*x, x*x*x))

# Interpolation

name = 'Bob'
print('Hello, {name}')

a = 5
b = 10
print(f'five plus ten is {a + b} and not {2 * (a + b)}')

def greet(name, question):
    return f"Hello, {name}! How is it {question}?"

print(greet("Bob", "going"))

def greet(name, question):
    return "Hello, " + name + "! How is it " + question + "?"

print(greet("Bob", "going"))