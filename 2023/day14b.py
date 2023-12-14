


def transpose(mat):
    rows = len(mat)
    cols = len(mat[0])
    mat2 = []
    for j in range(cols):
        col = []
        for i in range(rows):
            col.append(mat[i][j])
        mat2.append(col)
    return mat2


mat1 = []
with open("day14.txt", 'r') as f:

    for i,line in enumerate(f.readlines()):

        row = list(line.strip())
        if row:
            mat1.append(row)


mat2 = transpose(mat1)


def rotat(dir):

    s = 0

    if dir in ("N", "S"):
        mat = mat2
    else:
        mat = mat1

    cols = len(mat)
    rows = len(mat[0])

    if dir in ("N", "W"):
        onxt = 0
        incr = 1
        rev = False
    else:
        onxt = rows - 1
        incr = -1
        rev = True

    newm = {}
    for i in range(cols):
        col = mat[i]
        nxt = onxt

        _col = list(enumerate(col))
        if rev:
            _col.reverse()

        for j, ch in _col:
            if ch == '.':
                continue
            if ch == 'O':
                new_pos = nxt
                nxt = new_pos + incr
                newm[(i, j)] = (i, new_pos)

            if ch == '#':
                nxt = j + incr

    if dir in ("N", "S"):
        for (ocol, orow), (ncol, nrow) in newm.items():
            incr = rows - nrow  # this works because square matrix

            mat2[ocol][orow], mat2[ncol][nrow] = mat2[ncol][nrow], mat2[ocol][orow]
            mat1[orow][ocol], mat1[nrow][ncol] = mat1[nrow][ncol], mat1[orow][ocol]
            s += incr
    else:
        for (orow, ocol), (nrow, ncol) in newm.items():
            incr = rows - nrow

            mat2[ocol][orow], mat2[ncol][nrow] = mat2[ncol][nrow], mat2[ocol][orow]
            mat1[orow][ocol], mat1[nrow][ncol] = mat1[nrow][ncol], mat1[orow][ocol]
            s += incr

    return s

def printm():
    for row in mat1:
        print(" ".join(row))
    print("--------------")


def cycle():
    #printm()
    rotat("N")
    #print("after N")
    #printm()
    rotat("W")
    #print("after W")
    #printm()
    rotat("S")
    #print("after S")
    #printm()
    score = rotat("E")
    #print("after E")
    #printm()
    return score


import copy
import sys

BILL = 1000000000

previous_matrixes = []
for k in range(BILL):  # don't worry, we're not going to reach that
    sc = cycle()
    for j, _mat in enumerate(previous_matrixes):
        if _mat == mat1:
            print(f"Cycle {j+1} has same matrix as cycle {k+1}")
            diff = k - j # so it repeats every diff cycles
            to_bill = BILL - (k+1)
            if to_bill % diff == 0:
                print(f"Score at billion = {sc}")
                sys.exit(0)
    previous_matrixes.append(copy.deepcopy(mat1))
    print(f"After {k+1} cycles: {sc}")

