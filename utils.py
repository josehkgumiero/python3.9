def _pid(*_object):
    for _item in _object:
        print([id(_item)])
    print("""\n""")

import inspect

def _pvn(*var):
    for _item in var:
        callers_local_vars = inspect.currentframe().f_back.f_locals.items()
        print([var_name for var_name, var_val in callers_local_vars if var_val is _item])
    print("""\n""")

def _lal(_list_1, _list_2):
    for _item in _list_1:
        _list_2.append(_item)
    print("""\n""")
    return _list_2

def _ifi(_list_1, _list_2):
    _list_2 = [_item for _item in _list_1]
    print("""\n""")
    return _list_2

def _pvv(*_object):
    for _item in _object:
        print(_item)
    print("""\n""")

def _pfn():
    print(__file__.split("/")[-1].split(".")[0])
    print("""\n""")