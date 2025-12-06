import sys
from collections import defaultdict
from operator import add, mul
ans = 0
ingred = 0
rs = []
mat = []
mat2 = []

final = []

with open("input.txt", "r") as f:
    for j, line in enumerate(f.readlines()):
        line = line[:-1]#.split()
        row = list(line)
        mat.append(row)
        mat2.append(line.split())




mults = mat2[-1]
mat2 = mat2[:len(mat2)-1]
mat = mat[:len(mat)-1]
digs = []

print(mat2)
print(mat)

ro = len(mat)
co = len(mat[0])
for c in range(len(mat2[0])):

    maxx = 0
    for r in range(ro):
        maxx = max(maxx, int(mat2[r][c]))

    d = len(str(maxx))
    #print(f"for col={c} we have {d}")
    digs.append(d)

st = 0
for c in range(len(mat2[0])):
    if mults[c] == '+':
        op = add
        curr = 0
    else:
        op = mul
        curr = 1

    for c2 in range(st, st + digs[c]):
        num = 0
        for r in range(ro):
            print(r, c2)
            if len(mat[r]) <= c2 or mat[r][c2] == ' ':
                continue
            num = (num * 10) + int(mat[r][c2])
        print(num)
        print("-----")
        curr = op(curr, num)

    print(f"{curr}, {op}, {mults[c]}")

    ans+=curr
    st+=digs[c] + 1
    print("-----")


#print(mat)
print(ans)
print(mults)
