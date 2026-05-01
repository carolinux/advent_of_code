import sys
from collections import Counter, deque
import heapq as hq
fn = "input.txt"
#fn = "small.txt"


def read_mat(fn, func=int):
    mat = []
    with open(fn, 'r') as f:
        for line in f.readlines():
            row = list(line.strip())
            row = [func(x) for x in row]
            mat.append(row)
    return mat

def print_mat(mat):
    for row in mat:
        print("".join([str(x) for x in row]))

def get_neighs(mat, i, j):
    res = []
    r = len(mat)
    c = len(mat[0])
    for di,dj in [(1,0),(-1,0),(0,1),(0,-1)]:
        ni=i+di
        nj=j+dj
        if ni>=0 and ni<r and nj>=0 and nj<c:
            res.append((ni, nj))


    return res


def dj(start):
    dist = {}
    dist[start] = 0
    q = []
    hq.heappush(q, (0, start[0], start[1]))
    end = (len(mat)-1, len(mat[0])-1)
    while q:
        d, i, j = hq.heappop(q)
        #print(f"reached {i} {j}")
        if (i, j) == end:
            return d
        for ni,nj in get_neighs(mat, i, j):
            cand = d + mat[ni][nj]
            if (ni, nj) not in dist or dist[(ni, nj)] > cand:
                dist[(ni, nj)] = cand
                hq.heappush(q, (cand, ni, nj))




mat = read_mat(fn)
print_mat(mat)

ans = dj((0,0))



print(ans)
