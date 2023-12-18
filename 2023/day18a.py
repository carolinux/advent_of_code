
import sys

sys.setrecursionlimit(1000000)

DIRS = {
    'D': (1, 0),
    'U': (-1, 0),
    'L':(0, -1),
    'R': (0, 1)
}


s = 0
mat = []
fn = 'day18.txt'
#fn = 'small.txt'

curr = (0, 0)

pts = set()
pts.add(curr)


with open(fn, 'r') as f:

    for i,line in enumerate(f.readlines()):
        prev = curr
        dir, num, color = line.strip().split()
        num = int(num)
        x, y = curr
        dx, dy = DIRS[dir]
        for j in range(1, num+1):
            nx = x + j*dx
            ny = y + j*dy
            curr = (nx, ny)
            pts.add(curr)
        #print(f"New curr from {prev} {dir} {num} = {curr}")

minx = min([x for x,_ in pts])
maxx = max([x for x,_ in pts])
miny = min([y for _,y in pts])
maxy = max([y for _,y in pts])

def oob(x, y):
    if x<minx or y <miny or x>maxx or y>maxy:
        return True
    return False

import faulthandler
faulthandler.enable()
from collections import deque


def bfs(pt, visited):
    visited.add(pt)

    q = deque()
    q.append(pt)

    while q:
        x,y = q.popleft()
        # check if neighbour out of bounds
        # check if neighbour visited
        # check if neighbour in border
        for ch, (dx, dy) in DIRS.items():
            cx = x +dx
            cy = y + dy
            cpt = (cx, cy)
            if cpt in visited:
                continue
            if cpt in pts:
                continue
            if oob(cx, cy):
                return True
            visited.add(cpt)
            q.append(cpt)

    return False


start_pts = set()
for dx, dy in ((1,0),(-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1) , (0, 1), (0, -1)):
    start_pts.add((dx, dy))

print(start_pts)

print(minx, maxx)
print(miny, maxy)
print("starting....")
for pt in start_pts:
    if pt in pts:
        print(f"Point {pt} belongs to border, skipping")
        continue
    if oob(*pt):
        print("Already escaped")
    visited = set()
    escaped = bfs(pt, visited)
    if escaped:
        print(f"Point {pt} escaped")
        continue

    else:
        ans = len(visited) + len(pts)
        print(f"Lava cells: {ans}")
        break



# the visited and the len(pts)









