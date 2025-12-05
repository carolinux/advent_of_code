import sys
from collections import defaultdict
import functools as ft
ans = 0

with open("input.txt", "r") as f:
    for line in f.readlines():
        line = line.strip()
        nums = list(int(x) for x in line)

        @ft.lru_cache(maxsize=None)
        def rec(i, n, numchosen):
            if numchosen == 12:
                return 0
            if i == n:
                return -1

            pow = 12 - numchosen - 1
            cand1 = rec(i+1, n, numchosen)
            cand2 =  rec(i+1, n, numchosen+1)

            if cand1 == -1 and cand2 == -1:
                return -1
            cands = []
            if cand1 != -1:
                cands.append(cand1)
            if cand2 != -1:
                cands.append(cand2 + nums[i]*10**pow)

            return max(cands)



        best = rec(0, len(nums), 0)
        print(best)
        ans+=best
print(ans)
