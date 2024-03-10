from utils import _pid
from utils import _pvn
from utils import _pvv

l1 = [1, 2, 3]
l2 = []
l3 = []

def _pfn():
    print(__file__.split("/")[-1].split(".")[0])
    print("""\n""")

def main():
    _pfn()

if __name__ == '__main__':
    main()
    _pvn(l1, l2, l3)
    _pvv(l1, l2, l3)
    _pid(l1, l2, l3)

#lc = [_item for _item in l]

#_pid(l, lc)

#lc.clear()