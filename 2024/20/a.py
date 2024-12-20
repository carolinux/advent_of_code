
import math
import sys
import collections as coll

lines = 15


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


def bfs(curr, mat, dopath=False):
    visited = set()
    q = coll.deque()
    q.append((0,curr, [curr]))
    visited.add((curr))
    prev = {}
    prev[curr] = None
    while q:
        #print(q)
        dist, curr, path = q.popleft()
        if curr == end:
            return dist, path, prev
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = curr[0] + di, curr[1] + dj
            if 0 <= ni < len(mat) and 0 <= nj < len(mat) and (ni, nj) not in visited and mat[ni][nj] != '#':
                visited.add((ni, nj))
                if dopath:
                    path2 = path.copy()
                    path2.append((ni, nj))
                else:
                    path2 = []
                prev[(ni, nj)] = curr
                q.append((dist+1, (ni, nj), path2))

    return math.inf

refdist, path, _ = bfs(start, mat, dopath=True)
path = set(path)

cnt = coll.defaultdict(set)
for i in range(len(mat)):
    for j in range(len(mat[0])):
        if mat[i][j] != '#':
            continue

        #print(i, j)
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < len(mat) and 0 <= nj < len(mat[0]):
                if (ni, nj) in path:
                    prev = mat[ni][nj]
                    prev0 = mat[i][j]
                    mat[i][j] = '.'
                    cand, _, prevs = bfs(start, mat, dopath=False)
                    path2 = []
                    curr =  end
                    while curr is not None:
                        path2.append(curr)
                        curr = prevs[curr]

                    path2 = set(path2)

                    if cand < refdist and (i, j) in path2 and (ni, nj) in path2 and prevs[(ni, nj)] == (i, j):
                        #if cand-refdist == -64:
                        #    print(i, j, ni, nj)
                        #    print(path2)

                        canonical = [(i, j), (ni, nj)]
                        canonical.sort()
                        canonical = tuple(canonical)
                        cnt[refdist-cand].add(canonical)
                    mat[i][j] = prev0

ways = 0

for k in sorted(cnt.keys()):
    v = len(cnt[k])
    #print(cnt[k])
    print(f"we have {v} ways that save {k} steps")
    if k>=100:
        ways+= v

print(ways)


