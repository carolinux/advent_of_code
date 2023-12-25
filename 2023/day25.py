fn = 'day25.txt'
#fn = 'small.txt'

import sys

sys.setrecursionlimit(3000)
from collections import defaultdict
g = defaultdict(list)
nodes = set()

edges = set()

with open(fn ,'r') as f:
    for line in f.readlines():
        node, ch = line.strip().split(":")
        node = node.strip()
        ch = ch.strip().split(" ")
        ch = [c.strip() for c in ch]
        g[node].extend(ch)
        nodes.add(node)
        for c in ch:
            nodes.add(c)
            g[c].append(node)
            edges.add((c, node))

n = len(nodes)
root = node # whatever

edges = list(edges)


def dfs(v, par, missing):
    low[v] = timer[0]
    prev[v] = timer[0]
    timer[0] = timer[0]+1
    for w in g[v]:
        if w == par:
            continue
        if (v, w) in missing or (w, v) in missing:
            continue

        if prev[w] != -1:
            low[v] = min(low[v], prev[w])
            continue

        dfs(w, v, missing)
        low[v] = min(low[v], low[w])

        if (prev[v] < low[w]):
            # {node, ch} is a bridge
            bridges.append((v, w))


def dfs2(node, par, visited, missing):
    visited.add(node)
    ans = 0
    for ch in g[node]:
        if ch == par:
            continue
        if ch in visited:
            continue
        if (ch, node) in missing or (node, ch) in missing:
            continue

        ans += dfs2(ch, node, visited, missing)
    return 1 + ans

ix = 0
for i in range(len(edges)):
    for j in range(i+1, len(edges)):
        ix+=1
        if ix % 1000 == 0:
            print(f"Checked {ix} out of {len(edges) * len(edges)}")
        low = {node:-1 for node in nodes}
        prev = {node:-1 for node in nodes}

        timer = [0]

        bridges = []
        missing = [edges[i], edges[j]]
        dfs(root, None, missing)
        #assert len(bridges) < 2
        if len(bridges) == 1:
            print(f"Found :) {bridges}, {missing}")
            visited = set()
            missing.append(bridges[0])
            sizes = []
            for node in nodes:
                if node not in visited:
                    siz = dfs2(node, None, visited, missing)
                    sizes.append(siz)

            assert sum(sizes) == len(nodes)
            if len(sizes) == 2:
                print(sizes[0]*sizes[1])
                sys.exit(0)

# Ans: 533628, ran in 16 minutes
