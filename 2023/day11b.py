"""Forced to use prefix sum, otherwise would run out of memory.
Prefix sum ended up nicer and easier to write than actually expanding.
"""
mat = []

empty_rows = set()
empty_cols = set()

with open("day11.txt", 'r') as f:

    for i,line in enumerate(f.readlines()):
        mat.append(list(line.strip()))
        if set(mat[-1]) == {'.'}:
            empty_rows.add(i)

rows = len(mat)
cols = len(mat[0])

for j in range(cols):
    empty = True
    for i in range(rows):
        if mat[i][j] != '.':
            empty = False
            break
    if empty:
        empty_cols.add(j)

MILL = 1000000
psumr = []
for i in range(rows):
    row_val = MILL if i in empty_rows else 1
    if i == 0:
        psumr.append(row_val)
    else:
        psumr.append(row_val + psumr[-1])


psumc = []
for i in range(cols):
    col_val = MILL if i in empty_cols else 1
    if i == 0:
        psumc.append(col_val)
    else:
        psumc.append(col_val + psumc[-1])


def get_ps(l, r, a):
    """Get the dist between l and r in O(1)"""
    if l == r:
        return 0
    return a[r] - a[l]


print(f"Rows: {rows}, cols={cols}")

galaxies = []

for i in range(rows):
    for j in range(cols):
        if mat[i][j] == '#':
            galaxies.append((i, j))

s = 0
n = len(galaxies)

for i, (gi, gj) in enumerate(galaxies):

    for j in range(i+1, n):
        xi,xj = galaxies[j]
        dist = abs(get_ps(xi, gi, psumr)) + abs(get_ps(xj, gj, psumc))
        s+=dist

print(s)
