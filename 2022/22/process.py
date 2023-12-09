import sys
fn = sys.argv[1]

DIR = ('L', 'R')


rowranges = []
colranges = []

cols = 0
rows = 0
with open(fn, 'r') as f:
    for line in f:
        if line.strip() == '':
            break
        else:
            cols = max(cols, len(line)-1)
            rows+=1

    instructions = f.readline().strip()


print(instructions)
print(rows)
print(cols)

r = 0
rowranges = [  [[-2, -2]]  for _ in range(rows)]
colranges = [  [[-2, -2]]  for _ in range(cols)]
walls = set()
with open(fn, 'r') as f:
    for line in f:
        if line.strip() == '':
            break
        
        for c, val in enumerate(line):
            if val == " ":
                #print("???")
                continue
            if val == '#':
                walls.add((r,c))

            if val == '\n':
                break
            if rowranges[r][-1][1] == c - 1:
                rowranges[r][-1][1] = c
            else:
                rowranges[r].append([c,c])

            if colranges[c][-1][1] == r - 1:
                colranges[c][-1][1] = r
            else:
                colranges[c].append([r, r])



        r+=1

for i in range(len(rowranges)):
    rowranges[i] = rowranges[i][1:]
for i in range(len(colranges)):
    colranges[i] = colranges[i][1:]
print(rowranges)
print(colranges)


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

D = [(0,1), (1,0), (0, -1), (-1, 0)]

def rotate(dirstr, currdir):
    """get the new direction"""
    previ = None
    for i in range(4):
        cand = D[i]
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

    return D[ix]




pos = (0, rowranges[0][0][0])
print(f"initial pos {pos}")
dir = (0, 1)

for ins in instr:

    if ins in DIR:
        dir = rotate(ins, dir)
        continue
    for _ in range(ins):
        cand = (pos[0] + dir[0], pos[1] + dir[1])
        crow = cand[0]
        ccol = cand[1]
        if cand in walls:
            continue
        if dir in ((0,1), (0, -1)):
            # check rowranges
            crange = rowranges[crow][0]
            cmin = crange[0]
            cmax = crange[1]
            if ccol < cmin:
                ccol = cmax
            elif ccol > cmax:
                ccol = cmin



        if dir in ((1,0),(-1,0)):
            # check col ranges
            rrange = colranges[ccol][0]
            rmin = rrange[0]
            rmax = rrange[1]
            if crow < rmin:
                crow = rmax
            elif crow > rmax:
                crow = rmin


        # chek wall also
        cand = (crow, ccol)
        if cand in walls:
            continue
        pos = cand


print(f"Final pos {pos}, dir {dir}")

for i in range(4):
    if D[i] == dir:
        ix = i
        break

res = 1000 * (pos[0]+1) + 4 * (pos[1]+1) + ix
print(res)




