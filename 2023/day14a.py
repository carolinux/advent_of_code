


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


s = 0
_mat = []
with open("day14.txt", 'r') as f:

    for i,line in enumerate(f.readlines()):

        row = list(line.strip())
        if row:
            _mat.append(row)
print(_mat)

mat2 = transpose(_mat)

cols = len(mat2)
rows = len(mat2[0])

newm = {}

for i in range(cols):
    col = mat2[i]
    nxt = 0  # mispelled it to next :(
    for j, ch in enumerate(col):
        if ch == '.':
            continue
        if ch == 'O':
            new_pos = nxt
            nxt = new_pos + 1
            newm[(i, j)] = (i, new_pos)

        if ch == '#':
            nxt = j + 1


for (ocol, orow), (ncol, nrow) in newm.items():

    incr = rows - nrow
    #print(f"We have a boulder at {ncol} {nrow}")

    s+=incr


print(s)

