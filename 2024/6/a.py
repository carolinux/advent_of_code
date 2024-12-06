
rows = 130
mat = []
start = None
import sys

sys.setrecursionlimit(10000)
for i in range(rows):
    row = list(input().strip())
    mat.append(row)
    try:
        col = row.index('^')
        if col != -1:
            start = (i, col)
    except:
        pass


def pmat():
    for row in mat:
        print(''.join(row))



dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
visited = set()
def turn_right(dir):
    ix = dirs.index(dir)
    new_ix = (ix + 1) % 4
    return dirs[new_ix]

#pmat()
#print("=====")

def wander(curr, dir):
    x, y = curr
    visited.add(curr)
    mat[x][y] ="X"
    while True:
        next = x+ dir[0], y+dir[1]
        if next[0] <0 or next[0] >= len(mat) or next[1] <0 or next[1] >= len(mat[0]):
            return
        if mat[next[0]][next[1]] == '#':
            dir = turn_right(dir)
            #pmat()
            #print("=====")
        else:
            break
    wander(next, dir)



wander(start, dirs[0])
print(len(visited))

