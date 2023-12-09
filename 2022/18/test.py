

cube = [(2,2,2),
(1,2,2),
(3,2,2),
(2,1,2),
(2,3,2),
(2,2,1),
(2,2,3),
(2,2,4),
(2,2,6),
(1,2,5),
(3,2,5),
(2,1,5),
(2,3,5)]


cube = []
with open('cube.txt', 'r') as f:
    for line in f:
        parts = line.strip().split(',')
        triplet = []
        for part in parts:
            triplet.append(int(part))
        cube.append(tuple(triplet))


cube.sort()
print(cube)

cubeset = set(cube)

assert len(cube) == len(cubeset)

pts = len(cube)
overlaps = 0

for x,y,z in cube:
    if (x+1,y,z) in cubeset:
        overlaps+=1
    if (x,y,z+1) in cubeset:
        overlaps+=1
    if (x,y+1,z) in cubeset:
        overlaps+=1


print(f"Exposted surface = {pts*6 - 2* overlaps}")

