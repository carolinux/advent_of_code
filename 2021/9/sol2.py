import sys
from collections import Counter
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

def get_neighs(mat, i, j, coords=True):
    res = []
    r = len(mat)
    c = len(mat[0])
    if i-1>=0:
        if coords:
            res.append((i-1,j))
        else:
            res.append(mat[i-1][j])
    if i+1<r:
        if coords:
            res.append((i+1,j))
        else:
            res.append(mat[i+1][j])
    if j-1>=0:
        if coords:
            res.append((i,j-1))
        else:
            res.append(mat[i][j-1])
    if j+1<c:
        if coords:
            res.append((i,j+1))
        else:
            res.append(mat[i][j+1])
    return res

ans = 0
basins = set()

mat = read_mat(fn)
for i in range(len(mat)):
    for j in range(len(mat[0])):
        neighs = get_neighs(mat, i, j, False)
        if all([mat[i][j]<x for x in neighs]):
            basins.add((i,j))

def dfs(mat, i, j, vis):
    vis.add((i,j))
    for ni, nj in get_neighs(mat, i, j):
        if mat[ni][nj] == 9:
            continue
        if (ni,nj) in vis:
            continue
        dfs(mat, ni, nj, vis)

siz=[]
for basin in basins:
    vis = set()
    dfs(mat, *basin, vis)
    siz.append(len(vis))


siz.sort(reverse=True)
print(siz[0] * siz[1] * siz[2])
