
import math
import sys
import collections as coll


mat = [[math.inf for _ in range(71)] for _ in range(71)]
mp = {}

for i in range(3450):
    row, col = map(int, input().split(","))
    mat[row][col] = min(mat[row][col], i+1)
    mp[i+1] = (row,col)


def bfs(curr, mat, cutoff):
    visited = set()
    q = coll.deque()
    q.append((0,curr))
    visited.add((curr))
    while q:
        #print(q)
        dist, curr = q.popleft()
        if curr == (len(mat)-1, len(mat)-1):
            return dist
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = curr[0] + di, curr[1] + dj
            if 0 <= ni < len(mat) and 0 <= nj < len(mat) and (ni, nj) not in visited and mat[ni][nj] > cutoff:
                visited.add((ni, nj))
                q.append((dist+1, (ni, nj)))

l = 1024
r = 3451
while l < r:
    m = (l+r)//2
    if bfs((0, 0), mat, m) is None:
        r = m
    else:
        l = m+1


print(mp[l])


#34,32
