
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
    dists = {}
    dists[curr] = 0
    while q:
        #print(q)
        dist, curr, path = q.popleft()
        if curr == end:
            return dist, path, dists
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = curr[0] + di, curr[1] + dj
            if 0 <= ni < len(mat) and 0 <= nj < len(mat) and (ni, nj) not in visited and mat[ni][nj] != '#':
                visited.add((ni, nj))
                if dopath:
                    path2 = path.copy()
                    path2.append((ni, nj))
                else:
                    path2 = []
                dists[(ni, nj)] = dist+1
                q.append((dist+1, (ni, nj), path2))

    raise Exception("unreachabul")


def _dfs(curr, mat, termini, depth, res, vis):
    if curr in termini:
        res.append((curr, depth))
        return

    vis.add(curr)

    for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        ni, nj = curr[0] + di, curr[1] + dj
        if 0 <= ni < len(mat) and 0 <= nj < len(mat) and (ni, nj) not in vis:
            _dfs((ni, nj), mat, termini, depth+1, res, vis)


    vis.remove(curr)





def bfs2(st, mat, termini):
    visited = set()
    q = coll.deque()
    q.append((0,st))
    visited.add(st)
    res = {}

    while q:
        dist, curr = q.popleft()
        if dist>20:
            continue
        if curr in termini and dist>1:
            res[curr] = min(res.get(curr, math.inf), dist)
            continue
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = curr[0] + di, curr[1] + dj
            if 0 <= ni < len(mat) and 0 <= nj < len(mat) and (ni, nj) not in visited:
                visited.add((ni, nj))
                q.append((dist+1, (ni, nj)))

    return res

refdist, path, dists = bfs(start, mat, dopath=True)
path = set(path)

cnt = coll.defaultdict(set)

for pt1 in path:

    visited = bfs2(pt1, mat, path)
    for pt2, dist in visited.items():
        total = dists[pt1] + dist + (dists[end] - dists[pt2])
        if total < refdist:
            cnt[refdist-total].add(tuple([pt1, pt2]))


ways = 0

for k in sorted(cnt.keys()):
    v = len(cnt[k])
    #print(cnt[k])
    if k >=50:
        print(f"we have {v} ways that save {k} steps")
    if k>=100:
        ways+= v

print(ways)


