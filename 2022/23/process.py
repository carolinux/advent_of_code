import sys
fn = sys.argv[1]

from collections import Counter

row = 0
elves = 0

pos = {}
pix = 0 # ix of proposal
all_pos = set()
with open(fn, 'r') as f:
    for line in f:

        for col, ch in enumerate(line):
            if ch == '#':
                pos[elves] = (row, col)
                elves+=1
                all_pos.add((row, col))
        row-=1


rounds = 1000

D = ( (1, -1), (1,0), (1,1), (0, -1), (0, 1), (-1, -1), (-1, 0), (-1, 1))
dirs = ['N', 'S', 'W', 'E']

def get_ds(dir):
    if dir == 'N':
        return ((1, 0), (1, 1), (1, -1))
    if dir == 'S':
        return ((-1, 0), (-1, 1), (-1, -1))
    if dir == 'E':
        return ((0, 1), (1, 1), (-1, 1))
    if dir == 'W':
        return ((0, -1), (1, -1), (-1, -1))

def find_valid_cand(r, c, dir):
    ds = get_ds(dir)

    for dr, dc in ds:
        cand = (r + dr, c + dc)
        if cand in all_pos:
            return None
    
    dr, dc = ds[0]
    return r+dr, c+dc



def get_proposal(r, c):
    empty_neighs = []
    for dr, dc in D:
        if (r+dr, c+dc) not in all_pos:
            empty_neighs.append((r+dr, c+dc))

    if len(empty_neighs) == 8:
        return None, None

    for j in range(pix, pix+4):
        jj = j % 4
        dir = dirs[jj]

        res = find_valid_cand(r, c, dir)
        if res is not None:
            return res, dir

    #assert(False)
    return None, None
            
def pprint(all_pos):
    cnt = 0
    minr = min(p[0] for p in all_pos)
    maxr = max(p[0] for p in all_pos)
    minc = min(p[1] for p in all_pos)
    maxc = max(p[1] for p in all_pos)
    # (-3,0) north is up
    for i in range(maxr, minr-1, -1):
        col = []

        for j in range(minc, maxc+1):
            if (i, j) in all_pos:
                col.append('#')
            else:
                col.append('.')
                cnt+=1

        print(''.join(col))
    return cnt
    irint(all_pos)



pprint(all_pos)

for rix in range(rounds):


    propc = Counter()
    prope = {}
    for i in range(elves):
        r, c = pos[i]
        prop, dir = get_proposal(r, c)
        #print(f"for elf in pos {pos[i]}, porposed to go {dir} to {prop}, existing pos {pos}")
        prope[i] = prop
        propc[prop]+=1

    all_pos = set()
    moved = 0
    for i in range(elves):
        
        prop = prope[i]
        if prop is None:
            all_pos.add(pos[i])
            #print(f"elf at {pos[i]} didnt move")
            continue
        if propc[prop] == 1:
            # move elf to this position
            #print(f"move elf from {pos[i]} to {prop}")
            pos[i] = prop
            all_pos.add(prop)
            moved+=1

        else:
            all_pos.add(pos[i])
            #print(f"elf at {pos[i]} didnt move")
            continue

    print(f"After round {rix+1}")
    #pprint(all_pos)
    if moved == 0:
        print(f"Exited at round {rix+1}")
        sys.exit(0)




    pix+=1


empties = pprint(all_pos)
print("====================================================")
print(empties)
