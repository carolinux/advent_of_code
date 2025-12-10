import sys
import math
from collections import defaultdict, Counter
from operator import add, mul

pts = []
n = 0
with open("input.txt", "r") as f:
    for i, line in enumerate(f.readlines()):
        a,b = line.strip().split(',')
        pts.append((int(a),int(b)))

ans = 0
cs = []
for i, pt1 in enumerate(pts):
    for j, pt2 in enumerate(pts):
        if pt1 == pt2 or (i >=249 and j <249) or (j >=249 and i <249):
            continue


        maxx = max(pt1[0], pt2[0])
        minx = min(pt1[0], pt2[0])

        maxy = max(pt1[1], pt2[1])
        miny = min(pt1[1], pt2[1])
        bad = 0
        for pt3 in pts:
            xx, yy = pt3
            if minx < xx < maxx and miny <yy <maxy:
                bad = 1
                break

        if bad:
            continue

        cs.append((pt1, pt2))

        cand = (abs(pt1[0]-pt2[0])+1) * (1+abs(pt1[1]-pt2[1]))
        if cand > ans:
            print(f"{i} {j} {pt1} {pt2}")
        ans = max(ans, cand)
print(ans)
#print(cs)
