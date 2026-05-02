import sys
from collections import Counter, deque, defaultdict
import copy
fn = "input.txt"
#fn = "small.txt"


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
    if fn == "small.txt":
        return mat

    sigil = "#"
    for st in range(siz):
        for row in range(st, len(mat)-st):
            mat[row][st] = sigil
            mat[row][-st-1] = sigil

        for col in range(st, len(mat[0]) -st):
            mat[st][col] = sigil
            mat[-st-1][col] = sigil

        if sigil == "#":
            sigil = '.'
        else:
            sigil = "#"

    return mat


def print_mat(mat):
    for row in mat:
        print("".join([str(x) for x in row]))

def get_neighs(mat, i, j, iter, r0,c0,rx, cx):
    res = []
    r = len(mat)
    c = len(mat[0])
    for di,dj in [(-1,-1), (-1, 0), (-1, 1), (0,-1),(0,0),(0,1),(1,-1),(1,0),(1,1)]:
        ni=i+di
        nj=j+dj
        #if (ni == 0 or nj == 0 or ni == len(mat)-1 or nj == len(mat[0]) -1) and iter == 1:
        #    assert iter == 1
        #    res.append("#")
        #    continue
        if ni>=r0 and ni<rx and nj>=c0 and nj<cx:
            res.append(mat[ni][nj])
        else:
            if fn == "small.txt":
                res.append('.')
                continue
            if iter %2 == 0:
                res.append('.')
            else:
                res.append('#')
            #raise Exception(f"should not have gone oob -> {ni,nj} {len(mat)}x {len(mat[0])}")
    return res

def parse_vals(vals):
    num = 0
    assert len(vals) == 9
    for v in vals:
        num=num<<1
        if v == '#':
            num+=1
    return num


def compress(mat, i, j, iter,r0,c0, rows, cols):
    vals = get_neighs(mat, i, j, iter,r0,c0, rows, cols)
    #print(f"{vals} for {i},{j}")
    num = parse_vals(vals)
    new = key[num]
    #print(f"new: {new}")
    return new


def process(mat, r0, c0, rows, cols, iter):
    mat2 = copy.deepcopy(mat)
    for i in range(r0, rows):
        for j in range(c0, cols):
            new_val = compress(mat, i, j, iter, r0,c0, rows, cols)
            mat2[i][j] = new_val

    return mat2

ans = 0

key, mat = read_mat(fn)
r = len(mat)
c = len(mat[0])
origr = r
#print(key)

#print_mat(mat)
outerat = 50

mat = expand(mat, outerat)
print("expanded")
print_mat(mat)

r0 = outerat - 1
c0 = outerat - 1
rx = r0+r+2
cx = c0+c+2

for i in range(outerat):
    ans = 0
    print(f"start row {outerat-i-1}")
    print(f"{r0} to {rx}, {mat[1]}, {len(mat[0])}")
    print(f"size = {rx-r0}, origsize={origr}, step={i+1}")

    mat = process(mat, r0,c0, rx, cx, i)

    for ii in range(len(mat)):
        for jj in range(len(mat[0])):
            if ii<r0 or ii >= rx or jj<c0 or jj>=cx:
                #if i == 0 and fn !="small.txt":
                #    ans+=1
                #    mat[ii][jj] = "#"
                continue
            if mat[ii][jj] == "#":
                ans+=1
    #print("-------------------")
    #print(f"after iterat {i+1}: lit = {ans}")
    #print_mat(mat[:5])
    r0-=1
    c0-=1
    rx+=1
    cx+=1


print(ans)
#print(key[294])

