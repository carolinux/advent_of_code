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
for pt1 in pts:
    for pt2 in pts:
        if pt1 == pt2:
            continue

        cand = (abs(pt1[0]-pt2[0])+1) * (1+abs(pt1[1]-pt2[1]))
        ans = max(ans, cand)
print(ans)
