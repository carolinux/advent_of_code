import sys
from collections import defaultdict

s = 0
mat = []
fn = 'day20.txt'
#fn = 'small2.txt'

from dataclasses import dataclass


# parse the input and build the graph

g = defaultdict(list)
rg = defaultdict(list)


class Node:

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return self.id == other.id

    def __init__(self, id, ch, type):
        #print(id)
        self.id = id
        self.ch = ch
        self.n = len(ch)
        self.mem = []
        self.type = type
        self.state = 0
        self.mem = []


    def init_mem(self, incoming):
        if self.type !='&':
            return
        self.mem = {i:0 for i in incoming}

    def __repr__(self):
        return f"Node {self.id} with {self.n} children, type {self.type}, mem {self.mem}, state {self.state}"

    def process(self, inp, previous_id):
        emit = []  # list of (state, dest)
        if self.type == '%':
            if inp == 1:
                pass
            else:
                self.state = 1 - self.state  # turns off, sends low // turns on, sends high to all children
                for ch in self.ch:
                    emit.append((self.state, ch, self.id))
        elif self.type == '&':
            self.mem[previous_id] = inp
            if all(self.mem.values()):
                for ch in self.ch:
                    emit.append((0, ch, self.id))
            else:
                for ch in self.ch:
                    emit.append((1, ch, self.id))

        else: # broadcaster
            for ch in self.ch:
                emit.append((inp, ch, self.id))


        return emit

nodes = {}
with open(fn, 'r') as f:
    for line in f.readlines():
        line = line.strip()
        if line == "":
            continue
        id, ch = line.split("->")
        id = id.strip()
        ch = ch.strip().split(",")
        ch = [c.strip() for c in ch]
        if id != 'broadcaster':
            type = id[0]
            id = id[1:]
        else:
            type = 'root'
        #print(id, ch, type)
        node = Node(id, ch, type)
        nodes[id] = node
        g[node] = ch
        for c in ch:
            rg[c].append(node.id)

for node_id, incoming in rg.items():
    if node_id in ('output', 'rx'):
        continue
    node = nodes[node_id]
    node.init_mem(incoming)


depths = {}

sys.setrecursionlimit(1000000)

visited = set()

def dfs(node, dp):
    visited.add(node.id)
    print(node.id, dp)
    depths[node.id] = dp
    for ch in g[node]:
        if ch == 'rx':
            continue
        if ch in visited:
            continue
        dfs(nodes[ch], dp+1)

    return False

dfs(nodes['broadcaster'], 0)



#for node in g.items():
#    print(node)


from collections import deque
# lo hi
res = [0, 0]
prevres = [0, 0]
import copy
for it in range(1000):
    q = deque()
    q.appendleft((0, 'broadcaster', None))
    # add root to queue
    while q:
        state, node_id, par = q.pop()
        res[state]+=1
        #if node_id =='rx':
        #    print(f"rx state={state}")
        if node_id == 'rx' and state == 0:
            print(f"finished on iteration: {it+1}")
        if node_id in ('output', 'rx'):
            continue
        node = nodes[node_id]
        emit = node.process(state, par)

        q.extendleft(emit)

    #print(f"{it+1} finished with emissions: {res[0]-prevres[0]}, {res[1]-prevres[1]}")
    #print(nodes['bz'].mem)
    #input()
    #prevres = copy.copy(res)


"""

    dps = set()

    for node in g:
        if node.state == 1:
            dps.add(depths[node.id])

    print(f"At iteration {it} there are on % nodes at depths: {dps}")
    input()
"""





print(f"finished with emissions: {res}")
print(f"finished with emissions: {res[0] * res[1]}")
