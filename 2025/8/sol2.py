import sys
import math
from collections import defaultdict, Counter
from operator import add, mul
ans = 0

mat = []
pts = []
n = 0
with open("input.txt", "r") as f:
    for i, line in enumerate(f.readlines()):
        a,b,c = line.strip().split(',')
        pts.append((int(a),int(b),int(c), i))
        n+=1

def dist(a, b):
    x1, y1, z1, _ = a
    x2, y2, z2, _ = b
    x = (x1-x2)*(x1-x2)
    y = (y1-y2)*(y1-y2)
    z = (z1-z2)*(z1-z2)
    return x+y+z

dists = []
for i in range(n):
    for j in range(i+1, n):
        d = dist(pts[i], pts[j])
        dists.append((i, j, d))


dists.sort(key=lambda x: x[2])


class UnionFind:

    def __init__(self, n):
        self.par = list(range(n))
        self.rank = [0] * n
        self.size = [1] * n


    def find(self, a):
        if self.par[a] == a:
            return a
        self.par[a] = self.find(self.par[a])
        return self.par[a]


    def add(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b:
            print(f"{a} {b} already connected")
            return 0
        if self.rank[a] < self.rank[b]:
            b, a = a, b

        assert self.rank[a]>= self.rank[b]
        assert self.par[a] == a

        self.par[b] = a
        if self.rank[a] == self.rank[b]:
            self.rank[a]+=1
        self.size[a]+=self.size[b]
        self.size[b] = 0
        return 1


uf = UnionFind(n)
ix = 0
for i, j, _ in dists:
    #print(f"operation {ix} connecting {pts[i]} to {pts[j]}")
    assert i!=j
    new_conn  = uf.add(i, j)
    #print(uf.rank)
    ix+=1

    x = uf.find(i)

    if uf.size[x] == n:
        assert new_conn == 1
        print(pts[i])
        print(pts[j])
        ans = pts[i][0] * pts[j][0]
        print(ans)
        #print(uf.size)
        sys.exit(0)

### unreachabul ###
cnt = Counter()

for i in range(n):
    p = uf.find(i)
    cnt[p]+=1

cnts  = []
for k,v in cnt.items():
    cnts.append(v)

cnts.sort(reverse=True)
ans =1
for i in range(3):
    ans=ans * cnts[i]
print(ans)









