
rows = 10
rows = 130
mat = []
start = None
import sys

sys.setrecursionlimit(20000)
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

def wander(curr, dir, vis):
    x, y = curr
    if (curr, dir) in vis:
        return True # we got stuck in a loop
    visited.add((curr, dir))
    while True:
        next = x+ dir[0], y+dir[1]
        if next[0] <0 or next[0] >= len(mat) or next[1] <0 or next[1] >= len(mat[0]):
            return False  # we escaped
        if mat[next[0]][next[1]] == '#':
            dir = turn_right(dir)
            #pmat()
            #print("=====")
        else:
            break
    return wander(next, dir, vis)

ans = 0
for i in range(len(mat)):
    for j in range(len(mat[0])):
        print(f"at {i},{j}")
        val = mat[i][j]
        if val != '.':
            continue
        mat[i][j] = "#"
        visited=set()
        stuck = wander(start, dirs[0], visited)
        mat[i][j] = "."
        if stuck:
            ans+=1

print(ans)

