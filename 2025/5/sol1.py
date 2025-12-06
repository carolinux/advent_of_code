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
            rs.append((int(a), int(b)))


        elif line.strip() != "" and ingred == 1:
            item = int(line.strip())
            found = 0
            for a,b in rs:
                if item>=a and item <=b:
                    found = 1
                    break
                if found:
                    break
            if found:
                ans+=1


print(ans)
