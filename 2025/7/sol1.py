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

def rec(r,c):
    if r>=ro:
        return
    if c>=co or c<0:
        return
    if mat[r][c] == '.':
        rec(r+1, c)
        return
    if (r,c) in vsplit:
        return
    vsplit.add((r,c))
    if (r, c-1) not in vbeam:
        vbeam.add((r, c-1))
        rec(r, c-1)

    if (r, c+1) not in vbeam:
        vbeam.add((r, c+1))
        rec(r, c+1)

vbeam.add(start)
rec(start[0], start[1])
print(len(vsplit))
