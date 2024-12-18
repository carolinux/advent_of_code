
import math
import sys
import collections as coll


mat = [[math.inf for _ in range(71)] for _ in range(71)]


for i in range(1024):
    row, col = map(int, input().split(","))
    mat[row][col] = min(mat[row][col], i+1)


def bfs(curr, mat):
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
            if 0 <= ni < len(mat) and 0 <= nj < len(mat) and (ni, nj) not in visited and mat[ni][nj] == math.inf:
                visited.add((ni, nj))
                q.append((dist+1, (ni, nj)))

    return None


print(bfs((0, 0), mat))



