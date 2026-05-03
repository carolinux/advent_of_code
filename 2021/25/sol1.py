import sys
from collections import Counter, deque, defaultdict
import copy
fn = "input.txt"
#fn = "small.txt"

def read_mat(fn, func=str):
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


def process(mat):
    moves = 0
    mat2 = copy.deepcopy(mat)
    rows = len(mat)
    cols = len(mat[0])
    for i in range(rows):
        for j in range(cols):
            new_col = (j+1) % cols
            if mat[i][j] != ">":
                continue
            if mat[i][new_col] == '.':
                moves+=1
                mat2[i][j] = "."
                mat2[i][new_col] = ">"

    mat = mat2
    mat2 = copy.deepcopy(mat)

    for i in range(rows):
        for j in range(cols):
            new_row = (i+1) % rows
            if mat[i][j] != "v":
                continue
            if mat[new_row][j] == '.':
                moves+=1
                mat2[i][j] = "."
                mat2[new_row][j] = "v"
    return moves, mat2



mat = read_mat(fn)
print_mat(mat)
it = 0
while True:
    it+=1
    moves, mat = process(mat)
    if moves == 0:
        break

print(it)
