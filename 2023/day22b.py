import copy
from dataclasses import dataclass
from typing import List
from collections import deque

@dataclass(eq=True, order=True)
class Brick:
    x1: int
    y1: int
    z1: int
    x2: int
    y2: int
    z2: int
    id: int

    def __repr__(self):
        return f"Orientation: {self.orientation()}, id: {self.id}, x1,x2 = {self.x1},{self.x2}, y1,y2 = {self.y1},{self.y2}, z1,z2 = {self.z1},{self.z2}"

    def __init__(self, starts: List[int], ends: List[int], i: int):
        self.id = i
        self.x1, self.y1, self.z1 = starts
        self.x2, self.y2, self.z2 = ends
        if self.x1 > self.x2:
            self.x1, self.x2 = self.x2, self.x1
        if self.y1 > self.y2:
            self.y1, self.y2 = self.y2, self.y1
        if self.z1 > self.z2:
            self.z1, self.z2 = self.z2, self.z1
        self.stabilized = False

    # FIXME: fix off by one here, we can have unit cubes....
    def below(self): # the brick is supported by bricks that have an z2 == self.below and intersect
        return self.z1 - 1

    def above(self):
        return self.z2 + 1

    def orientation(self) -> str:
        if self.x1 != self.x2:
            return "H"
        if self.y1 != self.y2:
            return "D"  # for "depthy" eg it goes into the screen
        if self.z1 != self.z2:
            return "V"

    def fall_on(self, other):
        # we've found the highest brick that blocks current
        new_z1 = other.z2 + 1
        diff = self.z1 - new_z1
        self.z1-=diff
        self.z2-=diff
        self.stabilized = True
        return diff > 0

    def is_supported_by(self, other):
        #print("checking if", self, "is supported by", other)
        #print(f"self.below = {self.below()}, other.z2 = {other.z2}")
        if self.below() != other.z2:
            return False
        #print("checking if", self, "is supported by", other)
        return self.ix(self.x1, self.x2, other.x1, other.x2) and self.ix(self.y1, self.y2, other.y1, other.y2)

    def ix(self, s1, e1, s2, e2):
        disjoint = e1 < s2 or e2 < s1
        return not disjoint

    def is_blocked_by(self, other) -> bool:
        if other.z2 < self.z1:
            return self.ix(self.x1, self.x2, other.x1, other.x2) and self.ix(self.y1, self.y2, other.y1, other.y2)
        return False



fn = 'day22.txt'
#fn = 'small.txt'

brix = []
# add a bottom brick :)
with open(fn, 'r') as f:
    for i, line in enumerate(f.readlines()):
        coords = line.strip().split("~")
        starts = list(map(int, coords[0].split(",")))
        ends = list(map(int, coords[1].split(",")))
        br = Brick(starts, ends, i)
        brix.append(br)


# process the brix from lowest z1 to highest z1, and make them fall as far as they can

# once bricks have stabilized, for each brick check the neighbours that are directly above it
# for each neighbour, check the cnt of the below neighbours, if it is >1 for all, then the current brick can be demolished
dem = 0

import heapq as hq
q = []

for br in brix:
    hq.heappush(q, (br.z1, br))

while q:
    _, br = hq.heappop(q)
    if br.stabilized:
        continue
    blocked_by = Brick([0, 0, 0], [0, 0, 0], -1)  # the floor brick
    for br2 in brix:

        if br.id == br2.id:
            continue
        if br.is_blocked_by(br2):
            if br2.z2 >blocked_by.z2:
                blocked_by = br2
    #print(f"Brick {br} falls on {blocked_by}")
    changed = br.fall_on(blocked_by)
    assert blocked_by.id == -1 or br.is_supported_by(blocked_by)
    #print(br)


from collections import defaultdict

br2supported = {}
rg = defaultdict(list)
g = defaultdict(list)

for br in brix:
    cnt = 0
    for br2 in brix:
        if br.id == br2.id:
            continue
        if br.is_supported_by(br2):
            cnt+=1
            rg[br.id].append(br2.id)
            g[br2.id].append(br.id)

    br2supported[br.id] = cnt

skip = set()
for br in brix:
    can_dem = True
    for br2 in brix:
        if br.id == br2.id:
            continue
        if br2.is_supported_by(br) and br2supported[br2.id] == 1:
            can_dem = False
    if can_dem:
        skip.add(br.id)

s =0


def toposearch(brick, g, rg):
    out = copy.deepcopy(g)
    inc = copy.deepcopy(rg)
    visited = set()
    q = deque()
    q.append(brick.id)
    while q:
        br = q.popleft()
        if br in visited:
            continue
        visited.add(br)
        for nbr in out.get(br, []):
            inc[nbr].remove(br)
            if inc[nbr] == []:
                q.append(nbr)

    return len(visited) - 1

for brick in brix:
    if brick.id in skip:
        continue

    cnt = toposearch(brick, g, rg)
    s+=cnt

print(s)
