def parse_input(input_text):
    parts = input_text.strip().split("\n\n")
    matrix = [list(line) for line in parts[0].splitlines()]
    char_list = list(parts[1].strip())
    return matrix, char_list


import sys

input_text = sys.stdin.read()
mat, ops = parse_input(input_text)
mat2 = []
start = None
for i, row in enumerate(mat):
    row2 = []
    for ch in row:
        if ch == 'O':
            row2.append('[')
            row2.append(']')
        elif ch == '#':
            row2.append('#')
            row2.append('#')
        elif ch == '.':
            row2.append('.')
            row2.append('.')
        else:
            row2.append(ch)
            row2.append('.')
    mat2.append(row2)
    if '@' in row2:
        j = row2.index('@')
        mat2[i][j] = '.' # so that we can go there againe
        start = (i, j)

mat = mat2
mat[start[0]][start[1]] ='x'
for row in mat:
    print(''.join(row))
mat[start[0]][start[1]] ='.'



def canmovehor( curr, dir):
    ni, nj = curr[0] + dir[0], curr[1] + dir[1]
    if mat[ni][nj] == '#':
        return False
    if mat[ni][nj] == '.':
        return True
    return canmovehor((ni, nj), dir)

def movehor(curr, dir):

    ni, nj = curr[0] + dir[0], curr[1] + dir[1]
    assert mat[ni][nj] != "#"
    if mat[ni][nj] != '.':
        movehor((ni, nj), dir)
    #print(f"replacing {ni, nj} with {ch}")
    mat[ni][nj] = mat[curr[0]][curr[1]]
    mat[curr[0]][curr[1]] = '.'



def canmove(prev, curr, dir):
    ni, nj = curr[0] + dir[0], curr[1] + dir[1]
    ch = mat[curr[0]][curr[1]]
    if ch == ']':
        adjacent = (curr[0], curr[1]-1)
    else:
        adjacent = (curr[0], curr[1]+1)
    if mat[ni][nj] == '#':
        return False
    if mat[ni][nj] == '.':
        return True if adjacent == prev else canmove(curr, adjacent, dir)


    if prev == adjacent:
        return canmove(curr, (ni, nj), dir)
    return canmove(curr, (ni,nj), dir) and canmove(curr, adjacent, dir)

def move(prev, curr, dir):

    ni, nj = curr[0] + dir[0], curr[1] + dir[1]
    ch = mat[curr[0]][curr[1]]

    #print(f"Moving {curr} (value={ch})  into {dir} {mat[ni][nj]}")
    assert mat[ni][nj] != "#"
    if ch == ']':
        adjacent = (curr[0], curr[1]-1)
    else:
        adjacent = (curr[0], curr[1]+1)
    if mat[ni][nj] != '.':

        #print("adjacent is", adjacent)
        if prev == adjacent:
            move(curr, (ni, nj), dir)
        else:
            #print(f"will move {curr} into {dir} and {adjacent} into {dir}")
            move(curr, (ni,nj), dir)
            move(curr, adjacent, dir)
    elif prev != adjacent:
         move(curr, adjacent, dir)

    #print(f"replacing {ni, nj} with {curr}")
    mat[ni][nj] = ch
    mat[curr[0]][curr[1]] = '.'



def advance(curr, dir):
    ni = curr[0] + dir[0]
    nj = curr[1] + dir[1]

    if mat[ni][nj] == '.':
        return (ni, nj) # go to next thingey
    if mat[ni][nj] == '#':
        return curr # no movement
    assert mat[ni][nj] in ('[', ']')
    if dir[1] != 0:
        if canmovehor(curr, dir):
            movehor(curr, dir)
            return (ni, nj)
        return curr

    if canmove(None, (ni, nj), dir):
        #print("can move vertically yes")
        move(None, (ni, nj), dir)
        return (ni, nj)
    return curr


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
    #print(f"Operation: {op}")
    #for row in mat:
    #    print("".join(row))
    #mat[curr[0]][curr[1]] = '.'

score = 0
#print(mat)
for i in range(len(mat)):
    #print(f"{i}th row: {len(mat[i])}")
    for j in range(len(mat[i])):
        if mat[i][j] == '[':
            score+=(100*i) + j
print(score)

