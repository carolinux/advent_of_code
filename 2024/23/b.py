import sys
import math
from collections import defaultdict, Counter
from itertools import combinations as comb



def read_graph_from_stdin():
    g = defaultdict(set)

    for line in sys.stdin:
        parts = line.strip().split("-")
        a, b = parts
        g[a].add(b)
        g[b].add(a)
    return g


g = read_graph_from_stdin()

best_so_far = 2

# 520 nodes

# for each node, if it is part of the best cluster
# 3380 edges eg n * (n-1) / 2 <= 3380





print(len(g))
cnt_deg = Counter()
maxo = 1
for key in g:
    #print(key)
    #print(len(g[key]))
    maxo = max(maxo, len(g[key]))
    cnt_deg[len(g[key])]+=1

print(f"max outdeg={maxo}")
print(cnt_deg)

def combos(n, k):
    if n < k:
        return 0
    return math.factorial(n) // (math.factorial(k) * math.factorial(n-k))

maxcluster = 3
cand = 'foo'

for key in g:

    for i in range(maxcluster-1, len(g[key])+1):
        # i is the neighbours we take
        for combo in comb(g[key], i):
            good = True
            combo = list(combo)
            combo.append(key)
            for j in range(len(combo)):
                if not good:
                    break
                for k in range(j+1, len(combo)):
                    if combo[k] not in g[combo[j]]:
                        good = False
                        break
            if good and len(combo) > maxcluster:
                print(f"best so far {len(combo)}")
                maxcluster = max(len(combo), maxcluster)

                combo.sort()
                cand = ','.join(combo)



print(cand)
