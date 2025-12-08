
import math
import sys
import collections as coll

lines = 15


mat = []


for i in range(lines):
    row = list(input().strip())
    if 'S' in row:
        start = (i, row.index('S'))
        #row[row.index('S')] = '.'
    if 'E' in row:
        end = (i, row.index('E'))
        #row[row.index('E')] = '.'

    mat.append(row)


def bfs(curr, mat, dopath=False, targ=None):
    visited = set()
    q = coll.deque()
    q.append((0,curr, [curr]))
    visited.add((curr))
    dists = {}
    dists[curr] = 0
    while q:
        #print(q)
        dist, curr, path = q.popleft()
        if curr == targ:
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

    return math.inf, [], dists





def bfs2(st, mat, pathpts):
    visited = set()
    q = coll.deque()
    q.append((1, st, [st]))
    visited.add(st)
    res = {}

    while q:
        dist, curr, path2 = q.popleft()
        if dist>20:
            continue
        #assert not ( curr in termini and dist == 1)

        if curr in pathpts and dist > 1:
            assert dist>1
            res[curr] = dist
            continue
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = curr[0] + di, curr[1] + dj
            if 0 <= ni < len(mat) and 0 <= nj < len(mat[0]) and (ni, nj) not in visited:
                visited.add((ni, nj))
                newpath = path2.copy()
                newpath.append((ni, nj))
                q.append((dist+1, (ni, nj), newpath))

    return list(res.items())

refdist, path, dists = bfs(start, mat, dopath=True, targ=end)
#_, _, dists = bfs(end, mat, dopath=False)

cheats = {}

for i in range(len(mat)):
    for j in range(len(mat[0])):
        if mat[i][j] == '#':
            res = bfs2((i, j), mat, path)
            cheats[(i,j)] = res

cnt = coll.defaultdict(set)

for curr in path:
    #print(pt1)
    dist1 = dists[curr]
    for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        ni, nj = curr[0] + di, curr[1] + dj
        if 0 <= ni < len(mat) and 0 <= nj < len(mat[0]):
            for dest, dist in cheats.get((ni, nj),[]):
                cand = dist1 + dist + dists[end] - dists[dest]
                if cand <refdist:
                    if refdist - cand == 74:
                        print(f"Saving {refdist-cand} steps from {curr} to {dest} via {ni, nj}")
                        print(f"start-to-curr: {dist1}, curr-to-dest: {dist}, dest-to-end: {dists[end]-dists[dest]}")
                    cnt[refdist-cand].add((curr, dest))




ways = 0

for k in sorted(cnt.keys()):
    v = len(cnt[k])
    #print(cnt[k])
    if k >=50:
        print(f"we have {v} ways that save {k} steps")
        #print(cnt[k])
    if k>=100:
        ways+= v

print(ways)
sys.exit(0)

for pt1, pt2 in cnt[70]:
    mat2 = [row.copy() for row in mat]

    mat2[pt1[0]][pt1[1]] = 'X'
    mat2[pt2[0]][pt2[1]] = 'Y'

    print("---------")
    for ix, (i, j) in enumerate(pathz[(pt1, pt2)]):
        mat2[i][j] = str(ix+dists[pt1])

    for row in mat2:
        print(''.join(row))

    print("---------")
