import sys
from collections import Counter, deque
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
    for di,dj in [(1,1),(1,0),(-1,0),(-1,-1),(-1,1),(1,-1),(0,1),(0,-1)]:
        ni=i+di
        nj=j+dj
        if ni>=0 and ni<r and nj>=0 and nj<c:
            res.append((ni, nj))


    return res

def update(mat):
    q = deque()
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            mat[i][j]+=1
            if mat[i][j]>9:
                q.append((i, j))

    vis = set()
    while q:
        i, j = q.popleft()
        if (i, j) in vis:
            continue
        vis.add((i, j))
        for ni, nj in get_neighs(mat, i, j):
            mat[ni][nj]+=1
            if mat[ni][nj]>9 and (ni, nj) not in vis:
                q.append((ni, nj))

    for i,j in vis:
        mat[i][j] = 0

    return len(vis)



ans = 0

mat = read_mat(fn)
siz = len(mat) * len(mat[0])

for i in range(1000):
    flashes=update(mat)
    print(f"flashes in step{i+1}={flashes} out of {siz}")
    if flashes == siz:
        print("Found answer to part2!!!")
        sys.exit(0)
    ans+=flashes
    #print_mat(mat)


print(ans)
