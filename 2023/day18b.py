DIRS = {
    'D': (1, 0),
    'U': (-1, 0),
    'L':(0, -1),
    'R': (0, 1)
}


s = 0
mat = []
fn = 'day18.txt'
#fn = 'small.txt'

curr = (0, 0)

pts = set()
pts.add(curr)

import math
minx = math.inf
miny = math.inf
maxx = -math.inf
maxy = -math.inf

from collections import defaultdict

from dataclasses import dataclass

@dataclass
class Seg:
    x1: int
    y1: int
    x2: int
    y2: int
    dir: str
    id: int

segs = []
ddirs = []
num_border = 0

hrows = set()
with open(fn, 'r') as f:

    for i,line in enumerate(f.readlines()):
        prev = curr
        dir, num, hcolor = line.strip().split()
        num = int(num)

        color = hcolor[2:-1]
        color1 = int(color[:-1], 16)
        dir = color[-1]
        num = color1
        if dir == '0':
            dir = 'R'
        elif dir == '1':
            dir = 'D'
        elif dir == '2':
            dir = 'L'
        elif dir == '3':
            dir = 'U'

        #print(dir, num)
        #print(num, dir)
        ddirs.append(dir)
        px, py = prev
        dx, dy = DIRS[dir]
        x = px + dx
        y = py + dy

        cx = px + (dx * num)
        cy = py + (dy * num)
        curr = (cx, cy)
        minx = min(minx, cx,x)
        miny = min(miny, cy, y)
        maxx = max(maxx, cx, x)
        maxy = max(maxy, cy, y)
        if curr > prev:
            segs.append(Seg(x,y,cx,cy,dir, i))
        else:
            segs.append(Seg(cx,cy,x,y,dir, i))
        assert segs[-1].x1 <= segs[-1].x2
        assert segs[-1].y1 <= segs[-1].y2
        num_border+=num

        hrows.add(x-1)
        hrows.add(x)
        hrows.add(x+1)
        hrows.add(cx)
        hrows.add(cx+1)
        hrows.add(cx-1)



print(minx, maxx)
print(miny, maxy)

from dataclasses import dataclass

@dataclass(order=True, frozen=True)
class Crossing:
    min: int
    max: int
    dir: str
    pdir: str
    ndir: str

    def is_vert(self):
        return self.min == self.max and self.dir in ('U', 'D')

    def value(self):
        if self.is_vert():
            return 1
        if self.pdir == self.ndir:
            return 1
        return 0

# for each row, compute its crossings...
# all hsegs and all vsegs that intersect without turning in that row
# note that minimum should go one back etc


def get_crossings(r):
    res = []
    for i,seg in enumerate(segs):
        if seg.dir in ('L', 'R') and seg.x1 == r:

            assert seg.x1 == seg.x2

            y1 = seg.y1
            y2 = seg.y2

            if i == 0:
                pdir = segs[-1].dir
            else:
                pdir = segs[i-1].dir

            if i == len(segs) - 1:
                ndir = segs[0].dir
            else:
                ndir = segs[i+1].dir

            if i >0:
                if seg.dir == 'L':
                    y2+=1
                else:
                    assert(seg.dir == 'R')
                    y1-=1

            c = Crossing(y1, y2, seg.dir, pdir, ndir)
            res.append(c)

        elif seg.dir in ('U', 'D'):
            if seg.dir == 'D' and (r < seg.x1 or r >= seg.x2):
                continue
            if seg.dir == 'U' and (r <= seg.x1 or r > seg.x2):
                continue
            assert(seg.y1 == seg.y2)
            y1 = seg.y1; y2 = y1

            if i == 0:
                pdir = segs[-1].dir
            else:
                pdir = segs[i-1].dir

            if i == len(segs) - 1:
                ndir = segs[0].dir
            else:
                ndir = segs[i+1].dir

            c = Crossing(y1, y2, seg.dir, pdir, ndir)
            res.append(c)

    res.sort()
    return res


s = 0
incr = 0
for i, r in enumerate(range(minx, maxx+1)):

    if r not in hrows:
        s+=prev
        continue

    crossings = get_crossings(r)
    last_occ = None

    walls = 0
    incr = 0
    for cr in crossings:
        if last_occ is not None:
            num_occ = cr.min - last_occ - 1
        else:
            num_occ = 0
        last_occ = cr.max

        if walls % 2==1:
            s+= num_occ
            incr+=num_occ


        walls+= cr.value()
    #print(f"Line {r} has {incr} occupied cells")
    #print(f"and crossings = {crossings}")
    prev = incr
    print(f"After line {i} = {s} lava cells")
print(s+num_border)
#print(num_border)
#print(segs)

#952408144115 correct answer for sample
#62762509300678 correct answer for my input

# Unoptimized scanline took 19 minutes
# can probably make it faster by not looking at all the segments each time
