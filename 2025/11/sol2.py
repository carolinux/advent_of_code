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
vis.add("svr")

def paths(node, targ):
    if node == targ:
        #if "fft" in vis and "dac" in vis:
        #    print("good found")
        return 1
        #return 0

    ans = 0

    for ch in g[node]:
        if ch not in vis:
            vis.add(ch)
            ans+=paths(ch, targ)
            vis.remove(ch)
    #print(f"partial ans {ans}")
    return ans

#ans = paths("svr", "out")
#print(ans)
# dac->fft = 0
# dac -> out = 6141
# svr-fft
# fft-dac
sol1  = paths("fft", "dac")
print(sol1)
sys.exit(0)
#ans1 = paths("svr", "dac")
#print(ans1)ç
#ans2 = paths("dac", "fft")
#print(ans2)
ans3 = paths("fft", "out")
print(ans3)
ans4 = paths("svr", "fft")
print(ans4)
ans5 = paths("fft", "dac")
print(ans5)
ans6 = paths("dac", "out")
print(ans6)









