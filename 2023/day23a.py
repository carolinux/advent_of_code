from utils import read_str_mat, get_neighbours
from collections import deque, defaultdict


fn = 'day23.txt'
#fn = 'small2.txt'

badvals = '#'
mat = read_str_mat(fn)
rows = len(mat)
cols = len(mat[0])

start = (0, 1)
end = (rows-1, cols-2)

def has_cycles(par, curr, g, visited):
    visited.add(curr)
    for ch in g[curr]:
        if ch == par:
            continue
        if ch in visited:
            print(f"Cycle found at {ch}")
            return True
        res = has_cycles(curr, ch, g, visited)
        if res:
            return True
    return False


g = defaultdict(list)

for i in range(rows):
    for j in range(cols):
        if mat[i][j] == '#':
            continue
        if mat[i][j] == '.':
            neighs = get_neighbours((i,j), mat, None, badvals)
        elif mat[i][j] == '>':
            neighs = get_neighbours((i,j), mat, None, badvals, dirs=[(0,1)])
        elif mat[i][j] == '<':
            neighs = get_neighbours((i,j), mat, None, badvals, dirs=[(0,-1)])
        elif mat[i][j] == 'v':
            neighs = get_neighbours((i,j), mat, None, badvals, dirs=[(1,0)])

        g[(i,j)] = neighs

# the check is imperfect since we also can't go up from . to  a v for example
#assert not has_cycles(None, start, g, set())

import heapq as hq

dists = {pt: 0 for pt in g} # INIT
q = []
hq.heappush(q, (0, start, None))


while q:
    dist, pt, par = hq.heappop(q)
    #print(dist, pt, par, mat[pt[0]][pt[1]], g[pt])
    dist = -dist
    if dist < dists[pt]: # not the longest path then # CHECK
        continue
    if pt == end:
        continue

    for ch in g[pt]:
        if ch == par:
            continue
        cand = dist + 1
        if cand < dists[ch]: # CHECK
            continue
        dists[ch] = cand  # UPDATE
        hq.heappush(q, (-cand, ch, pt))

print(dists[end])
