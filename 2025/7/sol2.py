import sys
from collections import defaultdict
from operator import add, mul
ans = 0

mat = []
with open("input.txt", "r") as f:
    for r, line in enumerate(f.readlines()):
        line = line.strip()
        row = list(line)
        mat.append(row)
        try:
            ix = line.index('S')
            start = (r, ix)
        except:
            continue

ro = len(mat)
co = len(mat[0])
vsplit = set()
vbeam = set()

import functools as ft

@ft.lru_cache(maxsize=None)
def rec(r,c):
    if r>=ro:
        return 1
    if c>=co or c<0:
        return 0
    if mat[r][c] == '.':
        return rec(r+1, c)

    ret = 0
    ret+=rec(r, c-1)
    ret+=rec(r, c+1)
    return ret

ans = rec(start[0], start[1])
print(ans)

