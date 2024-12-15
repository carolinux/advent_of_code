def parse_input(input_text):
    parts = input_text.strip().split("\n\n")


    matrix = [list(line) for line in parts[0].splitlines()]
    char_list = list(parts[1].strip())
    return matrix, char_list


import sys

input_text = sys.stdin.read()
mat, ops = parse_input(input_text)

start = None
for i, row in enumerate(mat):
    if '@' in row:
        j = row.index('@')
        mat[i][j] = '.' # so that we can go there againe
        start = (i, j)
        break

print(start)

def advance(curr, dir):
    ni = curr[0] + dir[0]
    nj = curr[1] + dir[1]

    if mat[ni][nj] == '.':
        return (ni, nj) # go to next thingey
    if mat[ni][nj] == '#':
        return curr # no movement
    assert mat[ni][nj] == 'O'

    i, j = ni, nj

    while True:
        i+=dir[0]
        j+=dir[1]
        if mat[i][j] == '#':
            return curr
        if mat[i][j] == '.':
            mat[i][j] = 'O'
            mat[ni][nj] = '.'
            return (ni, nj)
        assert mat[i][j] == 'O'
    raise Exception("unreachable")

#for row in mat:
#    print("".join(row))
curr = start
for op in ops:
    if op == '\n':
        continue
    if op == '>':
        dir = (0, 1)
    elif op == '<':
        dir = (0, -1)
    elif op == '^':
        dir = (-1, 0)
    elif op == 'v':
        dir = (1, 0)

    curr = advance(curr, dir)
    #mat[curr[0]][curr[1]] = 'x'
    # print the matrix
    #for row in mat:
    #    print("".join(row))
    #mat[curr[0]][curr[1]] = '.'

score = 0
#print(mat)
for i in range(len(mat)):
    #print(f"{i}th row: {len(mat[i])}")
    for j in range(len(mat[i])):
        if mat[i][j] == 'O':
            score+=(100*i) + j
print(score)
print(len(ops))
print(set(ops))
