
import sys

sys.setrecursionlimit(1000000)

s = 0
mat = []
fn = 'day16.txt'
with open(fn, 'r') as f:

    for i,line in enumerate(f.readlines()):

        row = list(line.strip())
        if row:
            mat.append(row)

rows = len(mat)
cols = len(mat[0])



DIRS = {
    'N': (-1, 0),
    'S': (1, 0),
    'W':(0, -1),
    'E': (0, 1)
}

def get_new_dirs(ch, d):


    if ch == "/":
        if d == 'N':
            return ['E']
        elif d == 'E':
            return ['N']
        elif d == 'S':
            return ['W']
        elif d == 'W':
            return ['S']
    elif ch == "|":
        if d == 'N':
            return ['N']
        elif d == 'E':
            return ['S','N']
        elif d == 'S':
            return ['S']
        elif d == 'W':
            return ['S', 'N']

    elif ch == "-":
        if d == 'N':
            return ['E', 'W']
        elif d == 'E':
            return ['E']
        elif d == 'S':
            return ['E', 'W']
        elif d == 'W':
            return ['W']

    else:   # the case of \
        if d == 'S':
            return ['E']
        elif d == 'E':
            return ['S']
        elif d == 'N':
            return ['W']
        elif d == 'W':
            return ['N']


maxv = 0

starts = [(0, c, 'S') for c in range(cols)]
starts += [(rows-1, c, 'N') for c in range(cols)]
starts += [(r, 0, 'E') for r in range(rows)]
starts += [(r, cols-1, 'W') for r in range(rows)]

for start in starts:

    visited = set()


    def dfs(state):
        visited.add(state)
        x,y,d = state
        ch = mat[x][y]
        if ch == '.':
            new_dirs = [d]
        else:
            new_dirs = get_new_dirs(ch, d)

        for d1 in new_dirs:
            dx, dy = DIRS[d1]
            nx = x + dx
            ny = y + dy
            if nx <0 or ny <0 or nx>=rows or ny>=cols:
                continue
            new_state = (nx, ny, d1)
            if new_state in visited:
                continue
            dfs(new_state)


    dfs(start)

    visij = set()

    for i,j,d in visited:
        visij.add((i, j))

    if start == (0, 0, 'E'):
        print(f"Answer for part one: {len(visij)}")

    maxv = max(maxv, len(visij))

print(f"Answer for part two: {maxv}")








