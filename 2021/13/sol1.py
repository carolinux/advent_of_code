import sys
from collections import Counter, deque
fn = "input.txt"
#fn = "small.txt"


def read_mat(fn, func=int):
    mat = []
    cmds = []
    last_part = 0
    with open(fn, 'r') as f:
        for line in f.readlines():
            if line.strip() == "":
                last_part=1
                continue
            if last_part:
                instr = line.strip()
                p = instr.split("=")
                cmds.append((p[0][-1], int(p[1])))
                continue
            row = line.strip().split(",")
            row = [func(x) for x in row]
            mat.append(row)
    maxx=0
    maxy =0
    for y,x in mat:
        maxx=max(x, maxx)
        maxy = max(y, maxy)

    mat2 = [[0 for _ in range(maxy+1)] for i in range(maxx+1)]
    for y,x in mat:
        mat2[x][y] = 1

    return mat2, cmds

def print_mat(mat,r,c):
    for row in mat[:r]:
        print("".join(["#" if x ==1 else "." for x in row[:c]]))




ans = 0

mat, cmds = read_mat(fn)
#print_mat(mat)
rows = len(mat)
cols = len(mat[0])
for typ, fold in cmds:
    if typ == "y":
        y = fold
        diff = rows - y - 1
        for d in range(1, diff+1):
            for co in range(cols):
                #print(f"{y-d} vs {y+d}, diff ={d} out of {diff} y={y}, cols={cols}, rows={rows}")
                mat[y-d][co] = mat[y-d][co] | mat[y+d][co]
        rows = y
    else:
        x = fold
        diff = cols - x - 1
        for d in range(1, diff+1):
            for ro in range(rows):
                mat[ro][x-d] = mat[ro][x+d] | mat[ro][x-d]
        cols = x
    #break

# for part 1
#for i in range(rows):
#    for j in range(cols):
#        ans+=mat[i][j]
#print(ans)
print_mat(mat, rows, cols)
