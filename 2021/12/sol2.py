import sys
from collections import Counter, deque, defaultdict
fn = "input.txt"
#fn = "small.txt"

ans = 0


g = defaultdict(list)

with open(fn, "r") as f:
    for line in f.readlines():
        line = line.strip()
        parts = line.split("-")
        a = parts[0]
        b = parts[1]
        g[a].append(b)
        g[b].append(a)

# path is not necessary, but was good to debug with
def dfs(node, vis, path):
    #print(vis)

    if node == "end":
        #print(path)
        return 1

    res = 0
    for ch in g[node]:
        if ch in vis:
            continue
        if ch.lower() == ch:
            vis.add(ch)
        path.append(ch)
        res+=dfs(ch, vis, path)
        vis.discard(ch) # no error if not exists
        path.pop()
    return res



vis = set()
vis.add('start')
path = ["start"]
ans = dfs("start", vis, path)

print(ans)
