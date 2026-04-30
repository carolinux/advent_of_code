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

def get_neighs(mat, i, j):
    res = []
    r = len(mat)
    c = len(mat[0])
    if i-1>=0:
        res.append(mat[i-1][j])
    if i+1<r:
        res.append(mat[i+1][j])
    if j-1>=0:
        res.append(mat[i][j-1])
    if j+1<c:
        res.append(mat[i][j+1])
    return res

ans = 0

mat = read_mat(fn)
for i in range(len(mat)):
    for j in range(len(mat[0])):
        neighs = get_neighs(mat, i, j)
        if all([mat[i][j]<x for x in neighs]):
            ans+=1+mat[i][j]


print(ans)
