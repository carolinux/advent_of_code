import sys
from collections import defaultdict
from operator import add, mul
ans = 0
ingred = 0
rs = []
mat = []
with open("input.txt", "r") as f:
    for line in f.readlines():
        line = line.strip().split()
        row = list(line)
        mat.append(row)
print(mat[0])
mults = mat[-1]
mat = mat[:len(mat)-1]
ro = len(mat)
co = len(mat[0])
for c in range(co):
    if mults[c] == '+':
        op = add
        curr = 0
    else:
        op = mul
        curr = 1

    for r in range(ro):
        curr = op(curr, int(mat[r][c]))

    ans+=curr

#print(mat)
print(ans)
