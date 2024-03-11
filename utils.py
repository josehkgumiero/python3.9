def _pid(*_object):
    for _item in _object:
        print([id(_item)])
    print("""\n""")

def _rvn(*_object):
    return _object

def _rvv(*_object):
    _list = []
    for _item in _object:
        _list.append(_item)
    return _list

def _rvi(*_object):
    _list = []
    for _item in _object:
        _list.append([id(_item)])
    return _list
        
import inspect

def _pvn(*var):
    for _item in var:
        callers_local_vars = inspect.currentframe().f_back.f_locals.items()
        print([var_name for var_name, var_val in callers_local_vars if var_val is _item])
    print("""\n""")

def _lal(_list_1):
    _l = []
    for _item in _list_1:
        _l.append(_item)
    return _l

def _ifi(_list_1):
    return [_item for _item in _list_1]

def _lcl(_list_1):
    return _list_1.copy()

def _cll(_list_1):
    return list(_list_1)

def _sll(_list_1):
    return _list_1[:]

import copy

def _cop(_list_1):
    return copy.copy(_list_1)

def _pvv(*_object):
    for _item in _object:
        print(_item)
    print("""\n""")

def _pfn():
    print(__file__.split("/")[-1].split(".")[0])
    print("""\n""")




        