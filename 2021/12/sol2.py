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
def dfs(node, vis, path, used_twice):
    #print(vis)
    #print(path)
    if node == "end":
        #print(path)
        return 1

    res = 0
    for ch in g[node]:
        just_used_twice = False
        if ch in vis:
            if used_twice or ch =="start":
                continue
            just_used_twice = True
        if ch.lower() == ch:
            vis.add(ch)
        path.append(ch)
        res+=dfs(ch, vis, path, just_used_twice or used_twice)
        if not just_used_twice:
            vis.discard(ch) # no error if not exists
        path.pop()
    return res



vis = set()
vis.add('start')
path = ["start"]
ans = dfs("start", vis, path, False)

print(ans)
