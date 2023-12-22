import copy

from utils import read_str_mat, get_neighbours, print_mat
from collections import deque
import heapq as hq
import sys
import functools as ft

import matplotlib

matplotlib.use('GTK3Agg')

import matplotlib.pyplot as plt

def plot(mat):
    return
    mat3 = copy.deepcopy(mat)
    for i in range(len(mat3)):
        for j in range(len(mat3[0])):
            if mat3[i][j] == 'x':
                mat3[i][j] = 1
            else:
                mat3[i][j] = 0
    matrix = mat3
    rows, cols = len(matrix), len(matrix[0])

    fig, ax = plt.subplots(figsize=(100,100))

    cax = ax.matshow(matrix, cmap='viridis')

    for i in range(rows):
        for j in range(cols):
            print(i, j)
            ax.text(j, i, str(matrix[i][j]), ha='center', va='center', fontsize=12, color='black')

    for i in range(rows + 1):
        print(i)
        if i%FULL == 0:
            color = 'white'
        else:
            color = 'black'
        ax.axhline(i - 0.5, color=color, linewidth=2)

    for j in range(cols + 1):
        print(j)
        if j%FULL == 0:
            color = 'white'
        else:
            color = 'black'
        ax.axvline(j - 0.5, color=color, linewidth=2)

    print("colorbar")
    plt.colorbar(cax)
    #plt.show()
    print("save")
    plt.savefig('matrix.png')


#fn = 'day21.txt'
#fn = 'small2.txt'
small = False
if small:
    fn = 'small2.txt'
    HALF = 3
    FULL = 7
else:
    HALF = 65
    FULL = 131
    fn = 'day21.txt'
NN = 2
NN = 202300
badvals = '#'
mat = read_str_mat(fn)

for i in range(len(mat)):
    for j in range(len(mat[i])):
        if mat[i][j] == 'S':
            start = (i, j)

def find_reachable(starts, iter, parity, mat, verbose=False):
    q = deque()
    visited = set()
    for start in starts:
        q.append((0, start))
        visited.add(start)
    dists = {}

    while q:

        depth, pt = q.popleft()
        dists[pt] = depth
        if depth == iter:

            continue
        for ch in get_neighbours(pt, mat, visited, badvals):
            visited.add(ch)
            q.append((depth+1, ch))

    cnt = 0
    new_mat = copy.deepcopy(mat)
    #if verbose:
    #    print_mat(new_mat)
    for pt, d in dists.items():
        if d > iter:
            continue
        #rem = iter - d
        if d % 2 == parity:
            cnt+=1
            new_mat[pt[0]][pt[1]] = 'x'

    if verbose:

        #print_mat(new_mat)
        #print(cnt)
        plot(new_mat)
    cnt2 = 0
    for i in range(len(new_mat)):
        for j in range(len(new_mat[0])):
            if new_mat[i][j] == 'x':
                cnt2+=1
    #print(cnt2)
    #assert cnt==cnt2
    if verbose:
        return cnt, new_mat
    return cnt

rows = len(mat)
cols = len(mat[0])

ns = (0, start[1])
ss = (rows-1, start[1])
ws = (start[0], 0)
es = (start[0], cols-1)



LIMIT = HALF + (NN * FULL)

print(f"limit {LIMIT}")
# we start from zero at first, so we want paths with parity = 1
full1 = find_reachable([start], FULL, 1, mat)
full0 = find_reachable([start], FULL, 0, mat)


def ssum2(n):
    s = 0
    parity = 1
    for i in range(0,n+1):
        if i == 0:
            num = 1
        else:
            num = 4*i
        if parity:
            s+=num * full1
        else:
            s+=num * full0
        parity = 1 - parity
    print(f"last parity = {parity}, crust = {4*(i+1)}")
    return s, 4*(i+1), parity



n =  (LIMIT - HALF) // FULL

#assert n == 10



res1, crust,p = ssum2(n-1)
print(f"Find result for correct level ={res1}")

nn = find_reachable([ns], FULL, 1-p, mat)
sss = find_reachable([ss], FULL, 1-p, mat)
ee = find_reachable([es], FULL, 1-p, mat)
ww = find_reachable([ws], FULL, 1-p, mat)

wn = find_reachable([ws,ns], FULL, 1-p, mat)
sw = find_reachable([ws,ss], FULL, 1-p, mat)
ess = find_reachable([es,ss], FULL, 1-p, mat)
ne = find_reachable([es,ns], FULL, 1-p, mat)

ec = (0, 0)
wc = (0, cols-1)
nc = (rows-1, 0)
sc = (rows-1, cols-1)
# small crusts
wn1 = find_reachable([sc], HALF-1, 1-p, mat)
sw1 = find_reachable([wc], HALF-1, 1-p, mat)
ess1 = find_reachable([nc], HALF-1, 1-p, mat)
ne1 = find_reachable([ec], HALF-1, 1-p, mat)

res2 = 0
# add the partial
for cc in [wn, sw, ess, ne]:
    num = (crust-4)//4
    print(f"Crust per dir = {num}, cnt ={cc}")

    res2+= num * cc


for cc in [wn1, sw1, ess1, ne1]:
    num = (crust)//4
    print(f"small Crust per dir = {num}, cnt ={cc}")

    res2+= num * cc

print(f"ww={ww}, sss={sss}, ee={ee}, nn={nn}")
res2+=ww
res2+=sss
res2+=ee
res2+=nn



# 609012263058042 is the right answer

print(res1 + res2)
sys.exit(0)

# Code below does bruteforcing for a small number of expansions
# It helped me work out/visualize the parities and the partial boards

def stitch(mat, n):
    rowz2 = []
    for row in mat:
        if 'S' in row:
            row1 = copy.copy(row)
            row1[row.index('S')] = '.'
            row2 = n * row1 + row + n* row1
            #print(row2)
        else:
            row2 = (2*n+1) * row
        rowz2.append(row2)

    #print(f"I have {len(rowz2)}")
    mat2 = []
    for i in range(2 * n + 1):
        for r in rowz2:
            if i != n and 'S' in r:
                # print(f"removing s for {i}")
                r1 = copy.copy(r)
                r1[r.index('S')] = '.'
                mat2.append(r1)
            else:
                mat2.append(copy.copy(r))
        #print(mat2)

    print(f"Matrix = {len(mat2)} x {len(mat2[0])} ")
    for i in range(len(mat2)):
        for j in range(len(mat2[0])):
            if mat2[i][j] == 'S':
                start = (i, j)

    return mat2, start


mat2, start2 = stitch(mat, n)
#print_mat(mat2)
#print("----------")

res_comp, mat3 = find_reachable([start2], LIMIT, 1, mat2, verbose=True)
print(f" brute force {res_comp} vs {res1+res2}")


def get_cnt(mat2, i, j):
    cnt = 0
    #print(i)
    #print(j)
    for r in range(i, i+FULL):
        for c in range(j,j+FULL):
            if mat2[r][c] == 'x':
                cnt+=1
    return cnt

print("real segments")
for i in range(0, len(mat3), FULL):
    for j in range(0, len(mat3[0]), FULL):
            cnt = get_cnt(mat3, i, j)
            print(f"i={i}, j={j}, cnt={cnt}")






