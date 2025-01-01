import sys
import math
from collections import defaultdict



def read_graph_from_stdin():
    g = defaultdict(set)
    for line in sys.stdin:
        parts = line.strip().split("-")
        a, b = parts
        g[a].add(b)
        g[b].add(a)
    return g


def dfs(node, vis):
    vis.add(node)
    for ch in g[node]:
        if ch in vis:
            continue
        dfs(ch, vis)


def combos(n, k):
    if n < k:
        return 0
    return math.factorial(n) // (math.factorial(k) * math.factorial(n-k))


g = read_graph_from_stdin()


triplets = set()

for key in g:
    if len(g[key]) < 2 or key[0] != 't' :
        continue

    for ch1 in g[key]:
        for ch2 in g[key]:
            if ch1 == ch2:
                continue
            if ch1 in g[ch2]:
                li = [key, ch1, ch2]
                li.sort()
                triplet = tuple(li)
                triplets.add(triplet)


print(len(triplets))
