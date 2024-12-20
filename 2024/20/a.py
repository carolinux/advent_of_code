
import math
import sys
import collections as coll

lines = 141


mat = []


for i in range(lines):
    row = list(input().strip())
    if 'S' in row:
        start = (i, row.index('S'))
        row[row.index('S')] = '.'
    if 'E' in row:
        end = (i, row.index('E'))
        row[row.index('E')] = '.'

    mat.append(row)


def bfs(curr, mat, p1=None, p2=None):
    visited = set()
    q = coll.deque()
    q.append((0,curr, [curr]))
    visited.add((curr))
    prev = {}
    while q:
        #print(q)
        dist, curr, path = q.popleft()
        if curr == end:
            return dist, path
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = curr[0] + di, curr[1] + dj
            if 0 <= ni < len(mat) and 0 <= nj < len(mat) and (ni, nj) not in visited and mat[ni][nj] != '#':
                visited.add((ni, nj))
                path2 = path.copy()
                path2.append((ni, nj))
                q.append((dist+1, (ni, nj), path2))

    return math.inf

refdist, path = bfs(start, mat)
path = set(path)

cnt = coll.defaultdict(set)
for i in range(len(mat)):
    for j in range(len(mat[0])):

        print(i, j)
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < len(mat) and 0 <= nj < len(mat[0]):
                if (ni, nj) in path:
                    prev = mat[ni][nj]
                    prev0 = mat[i][j]
                    mat[i][j] = '.'
                    mat[ni][nj] = '.'
                    cand, path2 = bfs(start, mat)
                    path2s = set(path2)
                    if cand < refdist and (ni,nj) in path2s and (i,j) in path2s and path2.index((ni,nj)) == path2.index((i,j))+1:
                        #if cand-refdist == -64:
                        #    print(i, j, ni, nj)
                        #    print(path2)

                        canonical = [(i, j), (ni, nj)]
                        #canonical.sort()
                        canonical = tuple(canonical)
                        cnt[refdist-cand].add(canonical)
                    mat[ni][nj] = prev
                    mat[i][j] = prev0

ways = 0

for k in sorted(cnt.keys()):
    v = len(cnt[k])
    #print(cnt[k])
    print(f"we have {v} ways that save {k} steps")
    if k>=100:
        ways+= v

print(ways)


