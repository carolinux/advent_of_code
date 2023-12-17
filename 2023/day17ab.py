from dataclasses import dataclass
import sys
import heapq as hq


@dataclass(eq=True, frozen=True, order=True)
class State:
    r: int
    c: int
    d: str
    consec: int


s = 0
mat = []
fn = 'day17.txt'
#fn = 'small.txt'
with open(fn, 'r') as f:

    for i,line in enumerate(f.readlines()):

        row = list(line.strip())
        row = [int(x) for x in row]
        if row:
            mat.append(row)

rows = len(mat)
cols = len(mat[0])



DIRS = {
    'N': (-1, 0),
    'S': (1, 0),
    'W':(0, -1),
    'E': (0, 1)
}

MAX_CONSEC = 3 #for part 1
MIN_CONSEC = 0 #for part 1
MAX_CONSEC = 10
MIN_CONSEC = 4



def rev(d1, d2):
    if d1 == d2:
        return False
    x1, y1 = d1
    x2, y2 = d2

    if x1 ==x2 and y1 == -y2:
        return True
    if y1 == y2 and x1==-x2:
        return True
    return False

def get_neighs(state, rows, cols):

    neighs = []
    for d in DIRS.values():
        if d == state.d and state.consec == MAX_CONSEC:
            continue

        if d != state.d and state.consec < MIN_CONSEC:
            continue

        if rev(d, state.d):
           continue

        nr = state.r + d[0]
        nc = state.c + d[1]
        if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
            continue

        if d == state.d:
            new_state = State(nr, nc, d, state.consec + 1)
        else:
            new_state = State(nr, nc, d, 1)


        neighs.append(new_state)
    return neighs




# TODO: skip the visited ones (eg with set min dist)
# value == heat loss

# two start

dists = {}

q = []

start_state_down = State(0, 0, DIRS['S'], 0)
start_state_left = State(0, 0, DIRS['E'], 0)
hq.heappush(q, (0, start_state_down))
hq.heappush(q, (0, start_state_left))
dists[start_state_down] = 0
dists[start_state_left] = 0

# I wonder, can we re-visit a (r,c) cell as part of the optimal path?

while q:
    dist, state = hq.heappop(q)


    if state in dists and dists[state] < dist:
        continue
    if state.r == rows -1 and state.c == cols -1 and state.consec >= MIN_CONSEC:
        print(f"Min dist: {dist}")
        break
    for cand_state in get_neighs(state, rows, cols):
        cand_dist = dist + mat[cand_state.r][cand_state.c]
        if cand_state not in dists or dists[cand_state] > cand_dist:
            dists[cand_state] = cand_dist
            hq.heappush(q, (cand_dist, cand_state))
