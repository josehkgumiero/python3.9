def _function(**others):
    print(others)

_function(a = 1, b = 2, c = 3)

def _function_second(*args, **kwargs):
    print(args)
    print(kwargs)

_function_second(1, 2, x = 100, y = 200)

def _function_third(a, b, *, d, **kwargs):
    print(a)
    print(b)
    print(kwargs)

_function_third(1, 2, d = 20, x = 100, y = 200)

def _function_fourth(a, b, **kwargs):
    print(a)
    print(b)
    print(kwargs)

_function_fourth(1, 2, x = 100, y = 200)