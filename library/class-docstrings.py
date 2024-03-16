# help(print)

# help(int)

def _function(a, b = 1):
    """
    return a * b
    some additional docs here
    inputs:
    outputs:
    """
    return a * b

print(
    help(_function)
)

print(
    _function.__doc__
)

def _function_second(
    a: str = "annotation for a",
    b: str = "annotation for b"   
):
    """documentation for _function"""
    return print(a * b)

print(
    help(
        _function_second
    )
)

print(
    _function_second.__doc__
)

print(
    _function_second.__annotations__
)