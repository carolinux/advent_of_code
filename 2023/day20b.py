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

    def all(self) -> bool:
        return all(self.mem.values())

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
            type = 'r'
        #print(id, ch, type)
        node = Node(id, ch, type)
        nodes[id] = node
        g[node] = ch
        for c in ch:
            rg[c].append(node.id)

nodes['rx'] = Node('rx', [], 'r')
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
    #print(node.id, dp)
    depths[node.id] = dp
    for ch in g[node]:
        if ch == 'rx':
            continue
        if ch in visited:
            continue
        dfs(nodes[ch], dp+1)

    return False

dfs(nodes['broadcaster'], 0)


visited = set()
def dfs2(node, dp, f):
    visited.add(node.id)


    for ch in g[node]:
        if node.type == '&':
            nt = 'and_'
        elif node.type == '%':
            nt = 'or_'
        else:
            nt = node.type

        if nodes[ch].type == '&':
            nct = 'and_'
        elif nodes[ch].type == '%':
            nct = 'or_'
        else:
            nct = nodes[ch].type


        f.write(f"{nt}{node.id} -> {nct}{nodes[ch].id};\n")
        if ch in visited:
            continue
        dfs2(nodes[ch], dp+1, f)

    return False


with open("out.dot", 'w') as f:
    f.write("digraph G {\n")

    dfs2(nodes['broadcaster'], 0, f)

    f.write("}\n")



#for node in g.items():
#    print(node)


from collections import deque
# lo hi
res = [0, 0]
prevres = [0, 0]
import copy
ix = 0



for it in range(1000000):
    q = deque()
    q.appendleft((0, 'broadcaster', None))
    # add root to queue
    st = 0
    while q:
        ix+=1
        st+=1
        state, node_id, par = q.pop()
        res[state]+=1

        if node_id == 'rx' and state == 0:
            print(f"finished on iteration: {it+1},step={st}, total step={ix}")
        if node_id in ('output', 'rx'):
            continue
        node = nodes[node_id]
        emit = node.process(state, par)

        if node_id in  ('bz', 'gf', 'jj', 'xz'):

            # in my input (which I vizualized in day20.ps), those 4 nodes are required to emit 0 one after the other, without any of them emiting 1 in between
            #  used graphviz: dot -Tps out.dot -o day20.ps
            # res: 226732077152351 (the multiplication of the first time they emitted 0, each) -- technically lcm
            # I had to inspect the prints below to convince myself that it's OK to do this
            if node.all():
                # the goal
                print(f"AND node {node.id} will emit 0 now at {it+1}, step={st}, total step={ix}")
                #bz0.append(ix)
            else:
                pass
                #print(f"AND node {node.id} will emit 1 now at {it+1}, step={st}")
                #bz1.append(ix)

        q.extendleft(emit)


    #print(bz0)
    #print(bz1)
    #diffs = []
    #for k in range(1, len(bz1)):
    #    diffs.append(bz1[k] - bz1[k-1])

    #find_repeat(diffs)
    #input()
    #print(f"{it+1} finished with emissions: {res[0]-prevres[0] + res[1]-prevres[1]}")
    #print(nodes['xk'].state)
    #print(nodes['fb'].state)
    #print(nodes['gr'].state)
    #print(nodes['vj'].state)
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
