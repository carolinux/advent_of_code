from utils import read_str_mat, get_neighbours
from collections import deque, defaultdict
import sys

"""The idea here is to observe the input... Most of the time we put one foot in front of the other.
The junctions (where we have more than one option) are of a manageable number. So we can make a graph out of these (junction to junction) and
then look at ALL possible paths with dfs. I found 34 junctions in my input. 2^34 is a few billions, so even if all possible paths
were valid, we'd be looking at 17 billion paths. In reality it's less, the program finishes in ~10 seconds.
"""

fn = 'day23.txt'
#fn = 'small.txt'

badvals = '#'
mat = read_str_mat(fn)
rows = len(mat)
cols = len(mat[0])

start = (0, 1)
end = (rows-1, cols-2)

import sys

g = defaultdict(list)

for i in range(rows):
    for j in range(cols):
        if mat[i][j] == '#':
            continue
        neighs = get_neighbours((i,j), mat, None, badvals)
        g[(i,j)] = neighs


junctions = set()

for node, children in g.items():
    if len(children) >= 3:
        print(f"Node {node} has {len(children)} children")
        junctions.add(node)

print(len(junctions))
print(2**len(junctions))
junctions.add(start)
junctions.add(end)


def find_shortest(curr, jp, jp2, visited):
    visited.add(curr)
    if curr == jp2:
        return 0
    if curr !=jp and curr in junctions:
        return None
    for ch in g[curr]:
        if ch in visited:
            continue
        res = find_shortest(ch, jp, jp2, visited)
        if res is None:
            continue
        else:
            return res+1

    return None


edges = set()


for jp in junctions:
    print(jp)
    for jp2 in junctions:
        if jp == jp2:
            continue
        dist = find_shortest(jp, jp, jp2, set())
        if dist is not None:
            if jp < jp2:
                edges.add((jp, jp2, dist))


print(edges)
g2 = defaultdict(list)

for a,b, dist in edges:
    g2[a].append((b, dist))
    g2[b].append((a, dist))

mx = [0]


def dfs_longest(par, curr, targ, visited, dist):
    visited.add(curr)
    if curr == targ:
        mx[0] = max(mx[0], dist)
        visited.remove(curr)
        return

    for ch, d in g2[curr]:
        if ch == par:
            continue
        if ch in visited:
            continue
        dfs_longest(curr, ch, targ, visited, dist + d)

    visited.remove(curr)


dfs_longest(None, start, end, set(), 0)
print(mx[0])
