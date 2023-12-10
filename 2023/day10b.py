"""The idea here is instead of having 1 tile per cell, to have a 3x3 matrix per cell.
That way we can actually see the metallic creature squeeze between the d tiles of a pipe for example
(d for dot, n for the pipes)

d n d
d n d
d n d

Then, we do floodfill from the edges of the board.
Non nest tiles = Any reachable tiles via the floodfill + the tiles that have created the loop
So nest tiles = all tiles - non nest tiles

"""
mat = []
S = 'S'

n='n'
d='.'


L = [[d,n,d],
     [d,n,n],
     [d,d,d]]

J = [[d,n,d],
     [n,n,d],
     [d,d,d]]

F = [[d,d,d],
     [d,n,n],
     [d,n,d]]

SEV = [[d,d,d],
      [n,n,d],
      [d,n,d]]


PIPE = [[d,n,d],
        [d,n,d],
        [d,n,d]]

DASH = [[d,d,d],
        [n,n,n],
        [d,d,d]]


DOT = [[d,d,d],
        [d,d,d],
        [d,d,d]]


T =  [[d,d,d],
        [n,n,n],
        [d,n,d]]

import sys

import resource
resource.setrlimit(resource.RLIMIT_STACK, (resource.RLIM_INFINITY, resource.RLIM_INFINITY))

sys.setrecursionlimit(10000000)
print(sys.getrecursionlimit())


import faulthandler


faulthandler.enable()
starts = set()

fn = sys.argv[1]
mat0 = []
with open(fn, 'r') as f:


    for i,line in enumerate(f.readlines()):
        line = list(line.strip())
        mat0.append(line)
        line1=[]
        line2=[]
        line3=[]
        for j, ch in enumerate(line):
            if ch == 'F' or (ch == 'S' and (fn =='small.txt' or fn =='small3.txt' or fn == 'small4.txt' or fn == 'small5.txt')):
                triplet = F
            elif ch == 'J':
                triplet = J
            elif ch == 'L':
                triplet = L
            elif ch == '7':
                triplet = SEV
            elif ch == '|':
                triplet = PIPE
            elif ch == '-' or (ch == 'S' and (fn=='day10.txt')):  # in my input S is equivalent to -
                triplet = DASH
            elif ch == '.':
                triplet = DOT
            elif ch == 'S' and fn == 'small2.txt':
                triplet = T  # not really
            else:
                raise Exception(f"Invalid char {ch}")

            line1.extend(triplet[0])
            line2.extend(triplet[1])
            line3.extend(triplet[2])

            if ch == S:
                start = (i, j)
                for ii in range(3):
                    for jj in range(3):
                        if triplet[ii][jj] == n:
                            starts.add((3*i+ii,3*j+jj))

                print(starts)

        mat.append(line1)
        mat.append(line2)
        mat.append(line3)


rows = len(mat)
cols = len(mat[0])

free = set()
DIRS = [(0,1),(1,0),(-1, 0),(0, -1)]



from collections import deque
q = deque()
start = starts.pop()
q.append((0,start[0], start[1]))

mx = 0
visited1 = set()

while q:

    dist,x,y = q.popleft()

    if (x,y) in visited1:
        continue
    mx = max(dist, mx)
    visited1.add((x,y))
    if mat[x][y] !=n:
        raise Exception("")

    for dx, dy in DIRS:
        cx, cy = dx+x, dy+y
        if cx<0 or cy<0 or cx>=rows or cy>=cols:
            continue
        if (cx,cy) in visited1:
            continue
        if mat[cx][cy] != n:
            continue
        q.append((dist+1, cx, cy))


loop_coords = set([(i//3, j//3) for i,j in visited1])


def dfs(x, y, visited) -> bool:
    visited.add((x,y))
    prev = mat[x][y]
    for dx, dy in DIRS:
        cx, cy = x+dx, y+dy
        if cx<0 or cy<0 or cx>=rows or cy>=cols:
            continue
        if (cx,cy) in visited:
            continue

        curr = mat[cx][cy]
        if curr != d:
            continue
        dfs(cx, cy, visited)

    return


pts = set()

for i in range(rows):
    for j in range(3):
        pts.add((i, j))


for i in range(3):
    for j in range(cols):
        pts.add((i, j))
ix = 0
for i, j in pts:
    ix+=1
    if ix % 100 == 0:
        print(f"{ix} out of {len(pts)}")
    ii = i//3
    jj = j //3


    if (ii, jj) in loop_coords:
        free.add((i, j))
        continue

    if (i,j) in free:
        continue

    visited = {(i, j)}

    dfs(i, j, visited)

    for x,y in visited:
        free.add((x,y))

free2 = set()


for x,y in free:
    free2.add((x//3, y//3))


free2.update(loop_coords)
#print(len(free2))
print("Max dist:")
print(mx//3)
print("Nest cells:")
print((rows//3)*(cols//3) - len(free2))




