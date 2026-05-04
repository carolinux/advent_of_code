from funcs import BLOCKS as bl
import sys

"""
zs = {0}

for ix in range(12):
    zs2 = set()
    for w in range(1, 10):
        for z in zs:
            zs2.add(bl[ix](z, w))
    zs = zs2
    print(f"iter={ix+1}, len={len(zs)}, min={min(zs)}, max={max(zs)}")
    #print(zs)


sys.exit(0)
"""
import functools as ft
path = []

@ft.lru_cache(maxsize=None)
def recur(ix, z):
    if ix == 13:
        #print(path)
        for w in range(1, 10): # part1: 9,0,-1
            res = bl[ix](z, w)
            if res == 0:
                print(''.join([str(x) for x in path  +[w]]))
                raise Exception('found')
                return True
        return False
    for w in range(1, 10): # part1: 9,0,-1
        res = bl[ix](z, w)
        path.append(w)
        recur(ix+1, res)
        path.pop()
    return False


recur(0, 0)
