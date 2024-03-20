from utils import _pid
from utils import _pvn
from utils import _pvv
from utils import _lal
from utils import _ifi
from utils import _lcl
from utils import _cll
from utils import _sll
from utils import _cop

from utils import _rvv
from utils import _rvi
import pandas as pd 

l1 = [1, 2, 3]
l2 = []
l3 = []
l4 = []
l5 = []
l6 = []
l7 = []

_var = [['l1'], ['l2'], ['l3'], ['l4'], ['l5'], ['l6'], ['l7']]

_method = [['manual'], ['lal'], ['ifi'], ['lcl'], ['cll'],['sll'], ['cop']]

def _pfn():
    print(__file__.split("/")[-1].split(".")[0])
    print("""\n""")

def main():
    _pfn()

if __name__ == '__main__':
    main()

    _d = {}
    _d["""method"""] = _method
    _d["""name"""] = _var
    _d["""first_value"""] = _rvv(l1,l2,l3,l4,l5,l6, l7)
    _d["""first_id"""] = _rvi(l1,l2,l3,l4, l5,l6,l7)


    l2 = _lal(l1)
    l3 = _ifi(l1)
    l4 = _lcl(l1)
    l5 = _cll(l1)
    l6 = _sll(l1)
    l7 = _cop(l1)

    _d["""second_value"""] = _rvv(l1,l2,l3,l4, l5,l6, l7)
    _d["""second_id"""] = _rvi(l1,l2,l3,l4, l5,l6, l7)

    df = pd.DataFrame(_d)

    print(df)