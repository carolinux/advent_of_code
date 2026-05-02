import sys
from collections import Counter, deque, defaultdict
import copy
fn = "input.txt"
fn = "small.txt"


def read_mat(fn, func=str):
    mat = []
    key_read = 0
    with open(fn, 'r') as f:
        for line in f.readlines():
            if not key_read:
                key = line.strip()
                key_read = 1
                continue
            if line.strip() == "":
                continue
            row = list(line.strip())
            row = [func(x) for x in row]
            mat.append(row)
    return key, mat

def expand(mat, siz):
    # rows first
    cols = len(mat[0])
    mat = [['.'] * cols for _ in range(siz)] + mat + [['.'] * cols for _ in range(siz)]
    for i in range(len(mat)):
        str1 = ''.join(['.' for _ in range(siz)])
        str2 = ''.join(['.' for _ in range(siz)])
        mat[i] = list(str1) + mat[i] + list(str2)
    return mat


def print_mat(mat):
    for row in mat:
        print("".join([str(x) for x in row]))

def get_neighs(mat, i, j):
    res = []
    r = len(mat)
    c = len(mat[0])
    for di,dj in [(-1,-1), (-1, 0), (-1, 1), (0,-1),(0,0),(0,1),(1,-1),(1,0),(1,1)]:
        ni=i+di
        nj=j+dj
        if ni>=0 and ni<r and nj>=0 and nj<c:
            res.append(mat[ni][nj])
        else:
            raise Exception(f"should not have gone oob -> {ni,nj} {len(mat)}x {len(mat[0])}")
    return res

def parse_vals(vals):
    num = 0
    assert len(vals) == 9
    for v in vals:
        num=num<<1
        if v == '#':
            num+=1
    return num


def compress(mat, i, j):
    vals = get_neighs(mat, i, j)
    #print(f"{vals} for {i},{j}")
    num = parse_vals(vals)
    new = key[num]
    #print(f"new: {new}")
    return new


def process(mat, r0, c0, rows, cols):
    mat2 = copy.deepcopy(mat)
    for i in range(r0, rows):
        for j in range(c0, cols):
            new_val = compress(mat, i, j)
            mat2[i][j] = new_val

    return mat2

ans = 0

key, mat = read_mat(fn)
r = len(mat)
c = len(mat[0])
print(key)

#print_mat(mat)
outerat = 3
iterat = 2
mat = expand(mat, outerat)
print_mat(mat)


for i in range(2):
    ans = 0
    print(f"start row {outerat-i-1}")
    r0 = outerat-i-1
    c0 = outerat-i-1
    rx = r0+r+i+outerat
    cx = c0+c+i+outerat
    #print(f"{r0} to {rx}, {mat[0]}, {len(mat[0])}")

    mat = process(mat, r0,c0, rx, cx)

    for ii in range(len(mat)):
        for jj in range(len(mat[0])):
            if mat[ii][jj] == "#":
                ans+=1
    #print("-------------------")
    #print(f"after iterat {i+1}: lit = {ans}")
    #print_mat(mat)


print(ans)
#print(key[294])

