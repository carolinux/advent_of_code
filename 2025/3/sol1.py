import sys
from collections import defaultdict
ans = 0

with open("input.txt", "r") as f:
    for line in f.readlines():
        line = line.strip()
        nums = list(int(x) for x in line)
        index = defaultdict(list)
        for i in range(len(nums)):
            index[nums[i]].append(i)

        best = None

        for i in range(9, 0, -1):
            if best is not None:
                break
            if i not in index:
                continue
            for j in range(9, 0, -1):
                if j not in index:
                    continue
                if i == j and len(index[i]) == 1:
                    continue
                if index[j][-1]>index[i][0]:
                    best = (i*10) + j
                    ans+=best
                    break

print(ans)
