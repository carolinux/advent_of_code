import sys
from collections import defaultdict
ans = 0
ingred = 0
rs = []
with open("input.txt", "r") as f:
    for line in f.readlines():
        line = line.strip()
        if line.strip() == "":
            ingred = 1

        if line.strip() != "" and ingred == 0:
            # 334482514270603-336538665223902
            a, b = line.strip().split("-")
            rs.append([int(a), int(b)])




rs.sort()
disj = [rs[0]]

for i in range(1, len(rs)):
    prevend = disj[-1][1]
    cand = rs[i]
    if cand[0] > prevend:
        disj.append(cand)
        continue
    # otherwise
    disj[-1][1] = max(prevend, cand[1])


for a,b in disj:
    ans+= b-a+1


print(ans)
