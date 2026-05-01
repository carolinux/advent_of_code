import sys
from collections import Counter, deque, defaultdict
import copy
import heapq as hq

fn = "input.txt"
#fn = "small.txt"


def increment(mat):
    mat2 = copy.deepcopy(mat)
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            mat2[i][j]+=1
            if mat2[i][j] == 10:
                mat2[i][j] = 1
    return mat2


def read_mat(fn, func=int):
    mat = []
    with open(fn, 'r') as f:
        for line in f.readlines():
            row = list(line.strip())
            row = [func(x) for x in row]
            rows = [row]
            for i in range(4):
                nrow = [(x+1) if x+1<=9 else 1 for x in rows[-1]]
                rows.append(nrow)
            mat.append(rows[0] + rows[1] + rows[2] + rows[3] + rows[4])


    mat2 = increment(mat)
    mat3 = increment(mat2)
    mat4 = increment(mat3)
    mat5 = increment(mat4)

    return mat + mat2 + mat3 + mat4 + mat5

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
#print_mat(mat)

ans = dj((0,0))



print(ans)


#
#11637517422274862853338597396444961841755517295286
#11637517422274862853338597396444961841755517295286

#6755488935 3422155692453326671356443778246755488935
#6755488935 7866599146897761125791887223681299833479


#2274862853 2274862853338597396444961841755517295286
#2274862853 3385973964449618417555172952866628316397
