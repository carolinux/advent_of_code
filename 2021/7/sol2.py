import sys
from collections import Counter
fn = "input.txt"
#fn = "small.txt"



ans = 0
maxx = 0
maxy = 0
mat = []
arrows = []
with open(fn, 'r') as f:
    for line in f.readlines():
        nums = [int(x) for x in line.strip().split(",")]

s = sum(nums)
avg = s*1.0/len(nums)
print(avg)
avg = round(avg)
print(avg)

for avg in (avg, avg-1):#, avg-2, avg+1):

    ans = 0

    for num in nums:
        dist = abs(num-avg)
        ans+= (dist * (dist+1))>>1

    print(ans)

#101079875
#101079891
