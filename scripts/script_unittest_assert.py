def _function_add_int_numbers(x, y):
    assert isinstance(x, int) and  isinstance(y, int), "Both arguments must be integers."
    return x + y

print(_function_add_int_numbers(3, 5))
print(_function_add_int_numbers(3, "5"))

# python ./scripts/script_unittest_assert.py