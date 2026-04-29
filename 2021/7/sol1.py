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

#s = sum(nums)
#avg = s*1.0/len(nums)
nums.sort()
ix = len(nums)>>1
median = (nums[ix-1] + nums[ix]) /2.0

ans = 0

for num in nums:
    ans += abs(num-median)
print(ans)
print(median)
print(nums)
