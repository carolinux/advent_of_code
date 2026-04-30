import sys
from collections import Counter
fn = "input.txt"
#fn = "small.txt"




ans = 0

with open(fn, "r") as f:
    for line in f.readlines():
        parts = line.strip().split(" | ")
        outs = parts[1].split(" ")
        incr = 0
        for seg in outs:
            if len(seg) in (2,3,4,7):
                ans+=1
                if len(seg)!=7:
                    incr+=1
        print(incr)

print("========================")
print(ans)
