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

cnt = Counter(nums)
#print(cnt)

for i in range(256):
    cnt2 = Counter()
    for time_left, fish in cnt.items():
        #print(time_left)
        #print(fish)
        if time_left > 0:
            cnt2[time_left-1]+=fish
        else:
            assert time_left==0
            cnt2[6]+=fish
            cnt2[8]+=fish
    cnt = cnt2


print(sum(cnt.values()))


