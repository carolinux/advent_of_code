
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

curr = 'AAA'
steps = 0
print(ins)
while curr != 'ZZZ':
    ix = steps % len(ins)
    if ins[ix] == 'L':
        curr = graph[curr][LI]
    else:
        curr = graph[curr][RI]
    steps+=1
    if curr == 'ZZZ':
        break




print(steps)


