from collections import deque
import functools
import math

dist = {}
L = '<'
R = '>'
U = '^'
D = 'v'
A = 'A'
X = 'x'

DIR = [['x', '^', 'A'], ['<', 'v', '>']]

NUM = [['7','8','9'], ['4','5','6'], ['1','2','3'], ['x', '0', A]]


def get_cands(code):
    newseqs = []
    pos = 'A'
    for ch in code:
        seq1 = get_sp(pos, ch, directional=False)
        newseqs.extend(seq1)
        newseqs.append('A')
        pos = ch
    return [newseqs]


@functools.lru_cache(maxsize=None)
def get_codepaths(code):
    cands = []
    dir = NUM

    q = deque()
    q.append(((3,2), 0, []))
    minsofar = math.inf
    while q:

        curr, ix, path = q.popleft()
        if len(path) > minsofar:
            continue

        if ix == len(code):
            if len(path) < minsofar:
                cands = [path]
                minsofar = len(path)
            elif len(path) == minsofar:
                cands.append(path)
            continue

        ch = code[ix]
        if dir[curr[0]][curr[1]] == ch:
            new_ix = ix + 1
            path2 = path + [A]
            q.append((curr, new_ix, path2))
            continue
        else:
            new_ix = ix
            path2 = path

        # go right
        if curr[1] + 1 < len(dir[0]):
            if dir[curr[0]][curr[1]+1] != X:
                q.append(((curr[0], curr[1]+1), new_ix,  path2 + [R]))
        # go down
        if curr[0] + 1 < len(dir):
            if dir[curr[0]+1][curr[1]] != X:
                q.append(((curr[0]+1, curr[1]), new_ix,  path2 + [D]))

        # go up
        if curr[0] > 0:
            if dir[curr[0]-1][curr[1]] != X:
                q.append(((curr[0]-1, curr[1]), new_ix, path2 + [U]))

        # go left
        if curr[1] > 0:
            if dir[curr[0]][curr[1]-1] != X:
                q.append(((curr[0], curr[1]-1),  new_ix, path2 + [L]))

    return cands



@functools.lru_cache(maxsize=None)
def get_sp(p1, p2, directional=True):
    if p1 == p2:
        return []
    #print(f"Finding path from {p1} to {p2}")
    if directional:
        dir = DIR
    else:
        dir = NUM
    end = None
    for i in range(len(dir)):
        for j in range((len(dir[0]))):
            if dir[i][j] == p1:
                st = (i, j)
            if dir[i][j] == p2:
                end = (i, j)

    if end is None:
        raise Exception(f"Invalid end point {p2} in {dir}, p1={p1}")
    q = deque()
    q.append((st, []))
    while q:

        curr, path = q.popleft()

        if curr == end:
            #print(f"Found path {path}")
            return path

        # go right
        if curr[1] + 1 < len(dir[0]):
            if dir[curr[0]][curr[1]+1] != X:
                q.append(((curr[0], curr[1]+1), path + [R]))
        # go down
        if curr[0] + 1 < len(dir):
            if dir[curr[0]+1][curr[1]] != X:
                q.append(((curr[0]+1, curr[1]), path + [D]))

        # go up
        if curr[0] > 0:
            if dir[curr[0]-1][curr[1]] != X:
                q.append(((curr[0]-1, curr[1]), path + [U]))

        # go left
        if curr[1] > 0:
            if dir[curr[0]][curr[1]-1] != X:
                q.append(((curr[0], curr[1]-1), path + [L]))




# a robot moves on the number pad by >>>
# another robot sends the >>>>
# the first robot sends the >>> to the first robot
# and I send the commands to the first robot
ans = 0
codes = ['029A','980A','179A','456A','379A']
codes = ['208A', '586A', '341A', '463A', '593A']
for code in codes:

    cands = get_codepaths(code)
    print(f"Code={code}, cands={cands}, len={len(cands[0])}")
    minlen = math.inf



    for cand in cands:
        newseqs = []
        pos = 'A'
        for ch in cand:
            #print(f"Finding path from {pos} to {ch} at {i}")
            seq1 = get_sp(pos, ch)
            newseqs.extend(seq1)
            newseqs.append('A')
            pos = ch
        triplets = {}
        for i in range(len(newseqs)):
            if i+2 < len(newseqs):
                f = newseqs[i]
                s = newseqs[i+1]
                t = newseqs[i+1]
                triplets[(f,s,t)]+=1
            elif i+1 < len(newseqs):
                f = newseqs[i]
                s = newseqs[i+1]
                t = None
                triplets[(f,s,t)]+=1


        triplets[(A, 'v', '>')]+=1
        for i in range(2, 3): #(1, 26)
            count = 0

            for prev, ch, nxt in triplets:
                cnt = triplets[(prev, ch, nxt)]
                #print(f"Finding path from {pos} to {ch} at {i}")
                seq1 = get_sp(prev, ch)
                if nxt is not None:
                    seq2 = get_sp(ch, nxt)
                    seq2.append('A')
                else:
                    seq2 = None
                seq1.append('A')
                count+=len(seq1) * cnt
                for j in range(1, seq1):
                    diplet = (seq1[i-1], seq1[i])
            print(f"Code={code}, it={i}, len={len(seqs)} len={len(newseqs)} ratio={len(newseqs)/len(seqs)}")

            diplets = new_diplets

        minlen = min(minlen, count)

    ans+=minlen* int(code[:3])
    print(f"{minlen} x {int(code[:3])}")

print(ans)
