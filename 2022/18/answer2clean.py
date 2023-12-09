

import sys
fn = sys.argv[1]
cube = []
with open(fn, 'r') as f:
#with open('small.txt', 'r') as f:
    for line in f:
        parts = line.strip().split(',')
        triplet = []
        for part in parts:
            triplet.append(int(part))
        cube.append(tuple(triplet))



cubeset = set(cube)

pts = len(cube)
assert pts == len(cubeset)

deltas = ((0,0,1),(0,0,-1),(0,1,0),(0,-1,0),(1,0,0),(-1,0,0))
assert len(cube) == len(cubeset)


maxx = 0
maxy = 0
maxz = 0
minx = 100
miny = 100
minz = 100

for x,y,z in cubeset:
    maxx = max(x, maxx)
    maxy = max(y, maxy)
    maxz = max(z, maxz)
    minx = min(x, minx)
    miny = min(y, miny)
    minz = min(z, minz)
print(maxx)
print(maxy)
print(maxz)
print(minx)
print(miny)
print(minz)


def in_bounds(curr):
    x,y,z = curr
    return x>=minx and x <=maxx and y>=miny and y<=maxy and z>=minz and z<=maxz

def gn(x,y,z):
    res = []

    for dx,dy,dz in deltas:
        res.append((x+dx, y+dy, z+dz))

    return res

cands = set()
for x,y,z in cube:
    neighs = gn(x,y,z)
    for neigh in neighs:
        if neigh in cubeset:
            continue
        cands.add(neigh)
        assert neigh not in cubeset

print(f"Candidate bubbles {len(cands)}")


def dfs(curr, visited2):
    
    #print(visited2)
    assert curr not in cubeset
    visited.add(curr)
    x,y,z = curr
    neighs = gn(x,y,z)
    #print(x,y,z)

    ct = 0
    for neigh in neighs:
        if neigh in cubeset:
            ct+=1

    #print(f"The {curr} has {ct} neighbours that are solid")

    for neigh in neighs:
        if neigh in visited2 or neigh in cubeset:
            continue # cannot escape through here
        if in_bounds(neigh):
            visited2.add(neigh)
            res = dfs(neigh, visited2)
            if res:
                return True
        else:
            print(f"{neigh} is outside the lava, so we escaped")
            assert neigh not in cubeset
            return True

    # no direction gave us an escape
    # the bubble is trapped !
    return False


escaped = set()

for cand in cands:
    assert cand not in cubeset
    if cand in escaped:
        continue
    visited = set()
    print(visited)
    did_escape = dfs(cand, visited)
    if did_escape:
        for v in visited:
            escaped.add(v)


print(f"Escaped cands {len(escaped)}")
print(f"Trapped cands {len(cands-escaped)}")
trapped = cands - escaped

surface = 0
for x,y,z in cubeset:
    neighs = gn(x,y,z)
    for neigh in neighs:
        if neigh not in cubeset and neigh not in trapped:
            # the neighbour voxel is not a solid, and neither is it an internal bubble place, so the surface is exposed
            surface+=1


print(f"Exposed surface = {surface}")

