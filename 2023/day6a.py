from collections import defaultdict
import sys
mult = 1

with open("aoc6.txt", 'r') as f:
    times = f.readline().split(":")[1].split()
    dists = f.readline().split(":")[1].split()
import math

a = -1.0

for t, d in zip(times, dists):
    t = int(t)
    d = int(d)
    b = t
    c = -d
    root2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)
    root1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
    #print("Roots: ", root1, root2)
    if root1 == int(root1):
        root1 = root1 + 1
    else:
        root1 = int(math.ceil(root1))
    if root2 == int(root2):
        root2 = root2 - 1
    else:
        root2 = int(math.floor(root2))

    #print("Roots: ", root1, root2)
    multi = root2 - root1 + 1
    #print("Multi: ", multi)
    mult = mult * multi




#print(times)
#print(dists)

print(int(mult))
sys.exit(0)