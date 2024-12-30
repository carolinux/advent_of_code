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

        if len(path)> 10:
            raise Exception(f"Path too long at {curr}, {path}")
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
for code in codes:

    cands = get_cands(code)
    minlen = math.inf

    for cand in cands:
        seqs = cand
        for i in range(1, 3):
            newseqs = []
            pos = 'A'
            for ch in seqs:
                #print(f"Finding path from {pos} to {ch} at {i}")
                seq1 = get_sp(pos, ch)
                newseqs.extend(seq1)
                newseqs.append('A')
                pos = ch
            seqs = newseqs
            #print(f"for code={code}, it={i} path={newseqs}, len={len(newseqs)}")

        minlen = min(minlen, len(newseqs))

    ans+=minlen* int(code[:3])
    print(f"{minlen} x {int(code[:3])}")

print(ans)
