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
    if p1 == 'v' and p2 == 'A':
        return ['^','>']
    if p2 == 'v' and p1 == 'A':
        return ['<','v']
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

        # go down
        if curr[0] + 1 < len(dir):
            if dir[curr[0]+1][curr[1]] != X:
                q.append(((curr[0]+1, curr[1]), path + [D]))


        # go right
        if curr[1] + 1 < len(dir[0]):
            if dir[curr[0]][curr[1]+1] != X:
                q.append(((curr[0], curr[1]+1), path + [R]))


        # go up
        if curr[0] > 0:
            if dir[curr[0]-1][curr[1]] != X:
                q.append(((curr[0]-1, curr[1]), path + [U]))


        # go left
        if curr[1] > 0:
            if dir[curr[0]][curr[1]-1] != X:
                q.append(((curr[0], curr[1]-1), path + [L]))





from collections import Counter
from copy import copy
# a robot moves on the number pad by >>>
# another robot sends the >>>>
# the first robot sends the >>> to the first robot
# and I send the commands to the first robot
ans = 0
codes = ['029A','980A','179A','456A','379A']
codes = ['208A', '586A', '341A', '463A', '593A']
for code in codes:

    cands = get_codepaths(code)
    #print(f"Code={code}, cands={cands}, len={len(cands[0])}")
    minlen = math.inf

    for cand in cands:
        newseqs = []
        pos = 'A'
        for jj, ch in enumerate(cand):

            #print(f"Finding path from {pos} to {ch} at {i}")
            seq1 = get_sp(pos, ch)
            #print(f"Finding path from {pos} to {ch} at {i}={seq1}")
            newseqs.extend(seq1)
            newseqs.append('A')
            #print(f"at {jj}, len(newseqs)={len(newseqs)}")
            pos = ch

        diplets = Counter()
        for i in range(len(newseqs)):
            if i+1 < len(newseqs):
                f = newseqs[i]
                s = newseqs[i+1]
                diplets[(f,s)]+=1

        #print(f"it=1, code={code} len of sequence={len(newseqs)}, cand={cand}")
        first = newseqs[0]
        for i in range(2, 26):
            count = 0
            new_diplets = Counter()
            #print(f"{diplets} ofr {newseqs}")

            # the special diplet Av, doesnt prepend A

            for prev, ch in diplets:
                cnt = diplets[(prev, ch)]
                #print(f"Finding path from {pos} to {ch} at {i}")
                seq1 = get_sp(prev, ch)
                seq1 = seq1.copy()
                seq1.append('A')
                count+=len(seq1) * cnt
                for j in range(1, len(seq1)):
                    diplet = (seq1[j-1], seq1[j])
                    new_diplets[diplet]+=cnt

                new_diplets[(A, seq1[0])]+=cnt

            #new_diplets[(A, 'v')]+=1
            #print(f"Code={code}, it={i}, len={len(seqs)} len={len(newseqs)} ratio={len(newseqs)/len(seqs)}")

            diplets = new_diplets

            seq2 = copy(get_sp('A', first))
            seq2.append('A')
            count+=len(seq2)
            for j in range(1, len(seq2)):
                diplet = (seq2[j-1], seq2[j])
                new_diplets[diplet]+=1

            first = seq2[0]

        minlen = min(minlen, count)

    ans+=minlen* int(code[:3])
    print(f"{minlen} x {int(code[:3])}")

print(ans)

print(get_sp('A', '<'))
print(get_sp('<', 'A'))
print(get_sp('A', '^'))
print(get_sp('A', '>'))
print(get_sp('A', 'v'))

print(get_sp('^', 'v'))

# 414564774114120 too high

# 161427660668154 too low
# 176357262630721

# tried
#404564774114120 too high
#412430699844124
#412430699844124
#382430699844124
#604821067076159
#293023291027069
#293625167005328
