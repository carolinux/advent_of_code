
mat = []
S = 'S'

with open("day10.txt", 'r') as f:


    for i,line in enumerate(f.readlines()):
        mat.append(list(line.strip()))
        if S in mat[-1]:
            start = (i, mat[-1].index(S))


def rev(tupl):
    return (-tupl[0], -tupl[1])

rows = len(mat)
cols = len(mat[0])
# start from S, navigate in BFS for
# moves that are possible with pipes, legal and not visited (3 checks)

OUT = {'.':[], "-": [(0, 1), (0, -1)], "|": [(1,0), (-1, 0)], "F": [(0, 1), (1, 0)], "J": [(-1, 0), (0, -1)], "7":[(1, 0), (0, -1)], "L": [(0, 1), (-1, 0)], 'S': [(0,1),(0,-1),(1,0),(-1,0)]}

print(start)
print(mat)
from collections import deque
pos = start
q = deque()
q.append((0, pos))


mx = 0
visited = set()

while q:

    steps, pos = q.popleft()
    if pos in visited:
        continue
    visited.add(pos)
    x,y = pos

    mx = max(steps, mx)

    symbol = mat[pos[0]][pos[1]]
    for diff in OUT[symbol]:
        dx, dy = diff
        candx = x + dx
        candy = y + dy
        if candx<0 or candy<0 or candx>= rows or candy>=cols:
            continue

        symbol2 = mat[candx][candy]
        if rev(diff) in OUT[symbol2]:
            q.append((steps+1, (candx, candy)))






print(mx)


