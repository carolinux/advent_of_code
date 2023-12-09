import math
from collections import defaultdict


LI = 0
RI = 1

graph = defaultdict(list)


def sstr(s):
    return ''.join(s)

with open("aoc8.txt", 'r') as f:

    first = True

    for line in f.readlines():
        if first:
            ins = line.strip()
            first = False
            continue
        line = line.strip()
        if line == '':
            continue
        node = sstr(line[:3])
        left = sstr(line[7:10])
        right = sstr(line[12:15])
        graph[node].append(left)
        graph[node].append(right)

currs = []
for node in graph:
    if node[-1] == 'A':
        currs.append(node)


mults = []

steps = 0

while True:

    allz = True

    ix = steps % len(ins)
    newcurrs = []
    steps+=1
    for curr in currs:
        if ins[ix] == 'L':
            curr = graph[curr][LI]
        else:
            curr = graph[curr][RI]
        if curr[-1] != 'Z':
            newcurrs.append(curr)
        else:
            mults.append(steps)

    currs = newcurrs
    if not currs:
        break


res = math.lcm(*mults)




print(res)


