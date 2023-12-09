from copy import deepcopy
R = (0,1)
L = (0, -1)
U = (-1, 0) # reverted
D = (1, 0)
DIRS = [(0,1), (1,0), (0, -1), (-1, 0)]

NAMES: {R:'R', L:'L', D:'D', U:'U'}
def calculate(row, col, code):
    input()

    if code == 'LR':
        return L, row, MAX-col
    elif code == 'RL':
        return R, row, MAX-col
    elif code == 'DU':
        return D, MAX-row, col
    elif code == 'UD':
        return U, MAX-row, col
    elif code == 'LD':
        return U, MAX-col, MAX-row
    elif code == 'RU':
        return D, MAX-col, MAX-row
    elif code == 'UL':
        return R, col, row
    elif code == 'DR':
        return L, col, row
    elif code == 'LL':
        return R, MAX-row, 0
    elif code == 'RR':
        return L, MAX-row, MAX
    elif code == 'UU':
        return D, 0, MAX-col
    elif code == 'DD':
        return U, MAX, MAX-col
    elif code =='UR':
        return L, MAX-col, MAX-row
    elif code == 'DL':
        return R, MAX-col, MAX-row
    elif code == 'RD':
        return U, col, row
    elif code == 'LU':
        return D, col, row



    raise Exception()

import sys
fn = sys.argv[1]
if fn == 'small.txt':
    MAX = 3
else:
    MAX = 49

class Face:

    # neights = [alignment of left nb, nbid, right, up, down
    def __init__(self, id, tl, neighs):
        self.id = id
        self.tl = tl
        self.max = MAX
        self.walls = set()
        self.left = neighs[0:2]
        self.right = neighs[2:4]
        self.up = neighs[4:6]
        self.down = neighs[6:8]

    def is_wall(self, pt):
        return pt in self.walls

    def real_to_local(self, r, c):
        r1 = r - self.tl[0]
        c1 = c - self.tl[1]
        return r1,c1

    def local_to_real(self, r, c):
        r1 = r + self.tl[0]
        c1 = c + self.tl[1]
        return r1,c1

    def print(self):
        print(f"Face {self.id}")
        print(f"Num walls: {len(self.walls)}")

    def get_neigh_fid(self, dir):
        if dir == (0, 1):
            return int(self.right[1])
        if dir == (0, -1):
            return int(self.left[1])
        if dir == (1, 0):
            return int(self.down[1])
        if dir == (-1, 0):
            return int(self.up[1])

    def get_neigh_code(self, dir):
        if dir == R:
            return  'R'+ self.right[0]
        if dir == L:
            return  'L' + self.left[0]
        if dir == D:
            return  'D' + self.down[0]
        if dir == U:
            return 'U'+ self.up[0]

    def wrap(self, prev, dir):
        row, col = prev
        new_fid = self.get_neigh_fid(dir)
        code = self.get_neigh_code(dir)
        print(f"using code {code}")
        dir2, row2, col2 = calculate(row, col, code) 
        assert(row2>=0)
        assert(col2>=0)
        return new_fid , (row2, col2), dir2


    def exceeds(self, cand): # local coords
        r, c = cand
        return r<0 or r>MAX or c<0 or c>MAX

    def contains_real(self, r, c):
        maxr = self.tl[0]+MAX
        minr = self.tl[0]
        maxc = self.tl[1]+MAX
        minc = self.tl[1]
        #print(f"rows {minr}-{maxr} cols {minc}-{maxc} in face {self.id}")
        #print(r>=minr and r<=maxr)
        return r>=minr and r<=maxr and c>= minc and c<=maxc

    def add_wall(self, r, c):
        if self.contains_real(r, c):
            r1,c1 = self.real_to_local(r,c)
            self.walls.add((r1,c1))
            #print(f"Added wall {r,c} in face {self.id} in position {r1,c1}")
            return True
        else:
            #print(f"Wall {r,c} is not in face {self.id}")
            return False
if fn == 'small.txt':
    MAX = 3
    faces = []
    # LRUD neighboursFace 3

    # lrud
    faces.append(Face(1, (0,8), 'U3R6U2U4'))
    faces.append(Face(2, (4,0), 'D6L3U1D5'))
    faces.append(Face(3, (4,4), 'L2L4L1L5'))
    faces.append(Face(4, (4,8), 'R3U6D1U5'))
    faces.append(Face(5, (8,8), 'D3L6D4D2'))
    faces.append(Face(6, (8,12), 'R5R1R4R2'))
else:
    pass



DIR = ('L', 'R')


matrix = []

with open(fn, 'r') as f:
    for line in f:
        if line.strip() == '':
            break
        else:
            matrix.append(list(line[:-1]))

    instructions = f.readline().strip()


def parse_instructions(instr): # list int or tuple

    i = 0
    cnum = 0
    res = []
    while i < len(instr):
        ch = instr[i]
        if ch in DIR:
            res.append(cnum)
            res.append(ch)
            cnum = 0
        else:
            digit = int(ch)
            cnum = (cnum * 10) + digit
        i+=1

    res.append(cnum)

    return res


instr = parse_instructions(instructions)

print(matrix)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == '#':
            #print("===============")
            found = False
            for face in faces:
                tmp = face.add_wall(i,j)
                if tmp == True:
                    found = True

            if not found:
                raise Exception()

for face in faces:
    face.print()



def rotate(dirstr, currdir):
    """get the new direction"""
    previ = None
    for i in range(4):
        cand = DIRS[i]
        if cand == currdir:
            previ = i
            break

    assert(previ is not None)

    if dirstr == 'R':
        ix = previ + 1
    else:
        ix = previ - 1

    if ix == 4:
        ix = 0
    if ix == -1:
        ix = 3

    return DIRS[ix]



def advance(curr, faces):
    fid, pos, dir = curr
    face = faces[fid-1]
    cand = (pos[0] + dir[0], pos[1] + dir[1])
    if face.is_wall(cand):
        print(f'new place in same face {cand} is wall')
        return curr
    if face.exceeds(cand):
        print(f'{cand} exceeds bounds in face {fid}')
        new_curr = face.wrap(pos, dir)
        fid2, pos2, dir2 = new_curr
        if faces[fid2-1].is_wall(pos2):
            return curr
        return new_curr
    return fid, cand, dir

def find_containing_face(r,c):
    for face in faces:
        if face.contains_real(r,c):
            return str(face.id);
    return ' '


def pprint(curr):
    input()
    fid, pos, dir = curr
    face = faces[fid-1]
    r1, c1 = face.local_to_real(*pos)
    if dir == R:
        symbol = '>'
    elif dir == L:
        symbol = '<'
    elif dir == D:
        symbol = 'v'
    elif dir == U:
        symbol = '^'
    else:
        raise Exception()
    for i in range(len(matrix)):
        row = matrix[i]
        row = deepcopy(matrix[i])
        for j in range(len(matrix[i])):
            if row[j] == '.':
                fid2 = find_containing_face(i, j)
                row[j] = fid2
        if i == r1:
            row[c1] = symbol
            matrix[i][c1] = symbol

        print(''.join(row))

    print("============")



pos = (0, 0) # local pos
print(f"initial pos {pos}")
dir = (0, 1)
fid = 1
curr = (fid, pos, dir)
print(f"Instructions {instr}")
for ins in instr:
    fid, pos, dir = curr
    print(f"INstrictopns {ins}")
    if ins in DIR:
        dir = rotate(ins, dir)
        curr = (fid, pos, dir)
        print(f"========== ROTATED {ins}========")
        pprint(curr)
        continue
    for _ in range(ins):
        print("advancing")
        prev = curr
        curr = advance(curr, faces)
        if prev != curr:
            print(f"advanced to {curr} from {prev}")
            pprint(curr)


fid, pos, dir = curr
print(f"Final local pos {pos}, dir {dir}")

for i in range(4):
    if DIRS[i] == dir:
        ix = i
        break

r, c = faces[fid-1].local_to_real(*pos)
print(f"Final real pos {r,c}, dir {dir}")
res = 1000 * (r+1) + 4 * (c+1) + ix
print(res)




