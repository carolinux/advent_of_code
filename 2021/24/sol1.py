from funcs import BLOCKS as bl

"""
zs = {0}

for ix in range(12):
    zs2 = set()
    for w in range(1, 10):
        for z in zs:
            zs2.add(bl[ix](z, w))
    zs = zs2
    print(f"iter={ix+1}, len={len(zs)}, min={min(zs)}, max={max(zs)}")
"""


def recur(ix, z, path):
    if ix == 13:
        print(path)
        for w in range(1, 10):
            res = bl[ix](z, w)
            if res == 0:
                print(path  +[w])
                raise Exception("found:)")
        return
    for w in range(1, 10):
        res = bl[ix](z, w)
        path.append(w)
        recur(ix+1, res, path)
        path.pop()
    return


recur(0, 0, [])
