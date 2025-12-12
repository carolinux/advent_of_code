import sys
import math
from collections import defaultdict, Counter
from operator import add, mul
ans = 0
dunno = 0
no = 0

mat = []
pts = []
n = 0

areas = [7, 7, 6, 7, 7, 5]
with open("input.txt", "r") as f:
    for i, line in enumerate(f.readlines()):
        if i+1<31:
            continue
        parts = line.strip().split(":")
        assert parts[0][2] =='x'
        w = int(parts[0][:2])
        h = int(parts[0][3:])
        nums = parts[1][1:].split()
        nums = [int(x) for x in nums]
        assert len(nums) == 6
        #print(f"{line}, {w}x{h}, {nums}")
        areareq = 0
        for j in range(len(nums)):
            areareq+= nums[j] * areas[j]

        if w*h >= sum(nums) * 9:
            print("for sure yes")
            ans+=1

        elif w*h < areareq:
            print("for sure not")
            no+=1
        else:
            print("dunno")
            dunno+=1


print(f"dunno={no} out of {dunno+ans+no}")
print(ans)
