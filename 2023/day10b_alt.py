"""Alternative solution with a more complicated and error-prone flood fill.
Basically the reason I got stuck in this problem is because I did not understand that we should start on the "outside space" of an unused pipe
"""
mat = []
S = 'S'


yy='y'
n='n'
d='.'


L = [[yy,n,yy],
     [yy,n,n],
     [yy,yy,yy]]

J = [[yy,n,yy],
     [n,n,yy],
     [yy,yy,yy]]

F = [[yy,yy,yy],
     [yy,n,n],
     [yy,n,yy]]

SEV = [[yy,yy,yy],
      [n,n,yy],
      [yy,n,yy]]


PIPE = [[yy,n,yy],
        [yy,n,yy],
        [yy,n,yy]]

DASH = [[yy,yy,yy],
        [n,n,n],
        [yy,yy,yy]]


DOT = [[d,d,d],
        [d,d,d],
        [d,d,d]]


T =    [[yy,yy,yy],
        [n,n,n],
        [yy,n,yy]]

import sys

#sys.exit(0)
import resource
resource.setrlimit(resource.RLIMIT_STACK, (resource.RLIM_INFINITY, resource.RLIM_INFINITY))

sys.setrecursionlimit(10000000)
print(sys.getrecursionlimit())

# can proceed if neighbour = y or . or exceeds the bounds

# remember to /3 the coordinates and find the count

import faulthandler


faulthandler.enable()
starts = set()
#fn = "day10.txt"
fn = 'small2.txt'
fn="day10.txt"
fn = sys.argv[1]
mat0 = []
with open(fn, 'r') as f:


    for i,line in enumerate(f.readlines()):
        line = list(line.strip())
        mat0.append(line)
        line1=[]
        line2=[]
        line3=[]
        for j, ch in enumerate(line):
            if ch == 'F' or (ch == 'S' and (fn =='small.txt' or fn =='small3.txt' or fn == 'small4.txt' or fn == 'small5.txt')):
                triplet = F
            elif ch == 'J':
                triplet = J
            elif ch == 'L':
                triplet = L
            elif ch == '7':
                triplet = SEV
            elif ch == '|':
                triplet = PIPE
            elif ch == '-' or (ch == 'S' and (fn=='day10.txt')):  # in my input S is equivalent to -
                triplet = DASH
            elif ch == '.':
                triplet = DOT
            elif ch == 'S' and fn == 'small2.txt':
                triplet = T
            else:
                raise Exception(f"Invalid char {ch}")

            line1.extend(triplet[0])
            line2.extend(triplet[1])
            line3.extend(triplet[2])

            if ch == S:
                start = (i, j)
                for ii in range(3):
                    for jj in range(3):
                        if triplet[ii][jj] == n:
                            starts.add((3*i+ii,3*j+jj))

                print(starts)

        mat.append(line1)
        mat.append(line2)
        mat.append(line3)


rows = len(mat)
cols = len(mat[0])

nest = set()
free = set()
DIRS = [(0,1),(1,0),(-1, 0),(0, -1)]


from collections import deque
q = deque()
start = starts.pop()
q.append((0,start[0], start[1]))

mx = 0
visited1 = set()

while q:

    dist,x,y = q.popleft()

    if (x,y) in visited1:
        continue
    mx = max(dist, mx)
    visited1.add((x,y))
    if mat[x][y] !=n:
        raise Exception("")

    for dx, dy in DIRS:
        cx, cy = dx+x, dy+y
        if cx<0 or cy<0 or cx>=rows or cy>=cols:
            continue
        if (cx,cy) in visited1:
            continue
        if mat[cx][cy] != n:
            continue

        q.append((dist+1, cx, cy))


loop_coords = set([(i//3, j//3) for i,j in visited1])


def dfs(x, y, visited) -> bool:
    visited.add((x,y))
    prev = mat[x][y]
    if (x//3,y//3) in loop_coords and prev==n:
        print(f"reached some loop_coords at {x} {y}")
        raise Exception("should not happen")
    for dx, dy in DIRS:
        cx, cy = x+dx, y+dy
        if cx<0 or cy<0 or cx>=rows or cy>=cols:
            #print("reached out of bounds")
            return True
        if (cx,cy) in visited:
            continue



        curr = mat[cx][cy]
        if curr == n:
            continue

        cxx = cx//3
        cyy = cy//3

        same_pipe = (x//3 == cx//3) and (y//3 == cy//3)




        if (cx, cy) in free:
            return True


        esc = dfs(cx, cy, visited)
        if esc:
            #print("could escape")
            return True

    #print("could not escape")
    return False



#for row in mat:
#    print(''.join(row))



for i in range(rows):
    for j in range(cols):
        print(f"{i} {j} out of {rows} {cols}")
        ii = i//3
        jj = j //3
        if (ii, jj) in loop_coords:
            continue

        #if mat[i][j] not in (d, n):
        #    continue
        if (i,j) in free:
            continue
        if (i, j) in nest:
            continue
        visited = set()
        #reach_start = mat[i][j] == n
        #if reach_start:
        #    print(f"looking at pipe part at {i}, {j}")

        #if i!=12 or j!=34:
        #    continue

        escaped = dfs(i, j, visited)
        #print(visited)
        if escaped:
            for x,y in visited:
                #if mat[x][y] in (d, n):
                free.add((x,y))
        else:
            #nest.add((i, j))
            for x,y in visited:
                #if mat[x][y] in (d, n):
                nest.add((x,y))


nest2 = set()

for x,y in nest:
    #if mat[x][y] in (d, n):
    if (x//3, y//3) not in loop_coords:
        nest2.add((x//3, y//3))




import copy
mat2 = copy.deepcopy(mat)

for i in range(rows):
    for j in range(cols):
        if (i, j) in nest:
            mat2[i][j] ='I'
        #elif  mat[i][j] == yy:
        #    mat2[i][j] ='.'
        ii = i//3
        jj = j//3
        if (ii, jj) in loop_coords and mat[i][j] == n:
            mat2[i][j] = 'x'

for row in mat2:
    print(''.join(row))


for i,row in enumerate(mat0):
    for j, ch in enumerate(row):
        if (i,j) in loop_coords:
            mat0[i][j] = 'x'

    print(''.join(mat0[i]))


print(len(nest2))
print(f"Loop contains {len(loop_coords)} out of {len(mat0)*len(mat0[0])}")
print(f"maxidst: {mx//3}")





