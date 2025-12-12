import sys
import math
from collections import defaultdict, Counter
from operator import add, mul
ans = 0

g = defaultdict(list)
with open("input.txt", "r") as f:
    for i, line in enumerate(f.readlines()):
        parts = line.strip().split(":")
        #print(parts[0])
        children = parts[1][1:].split()
        #print(children)
        g[parts[0]].extend(children)


vis = set()
vis.add("you")

def paths(node):
    if node == "out":
        return 1
    ans = 0

    for ch in g[node]:
        #if ch not in vis:
        #vis.add(ch)
        ans+=paths(ch)
        #vis.remove(ch)


    return ans

ans = paths("you")
print(ans)









