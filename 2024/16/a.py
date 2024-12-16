from collections import deque
import heapq as hq
import math

E = (0, 1)
W = (0, -1)
N = (-1, 0)
S = (1, 0)

def get_cands(i, j, dir):

    cands = []
    for dx,dy in [dir]:
        cx, cy = i+dx, j+dy
        if cx < 0 or cx >= len(mat) or cy < 0 or cy >= len(mat[0]):
            continue
        if mat[cx][cy] == '#':
            continue
        cands.append((1, (cx, cy), dir))

    if dir in (E, W):
        cands.append((1000, (i, j), N))
        cands.append((1000, (i, j), S))
    else:
        cands.append((1000, (i, j), E))
        cands.append((1000, (i, j), W))

    return cands



def dj(i, j):
    dists = {}
    q = []
    hq.heappush(q, (0, (i, j), E))

    while q:
        cdist, pt, dir = hq.heappop(q)
        if mat[pt[0]][pt[1]] == 'E':
            return cdist

        cands = get_cands(*pt, dir)
        for incr, candpt, canddir in cands:
            key = (candpt, canddir)
            canddist = cdist + incr
            if key in dists and dists[key] <= canddist:
                continue
            dists[key] = canddist
            hq.heappush(q, (canddist, candpt, canddir))

    return math.inf


import sys

input_text = sys.stdin.read()
mat = [list(line) for line in input_text.splitlines()]
#print(mat)
ans = math.inf
for i in range(len(mat)):
    for j in range(len(mat[i])):
        if mat[i][j] != "S":
            continue
        cand = dj(i, j)
        ans = min(cand, ans)

print(ans)
