import sys
import math
import re
from collections import defaultdict, Counter
from operator import add, mul
import heapq as hq
ans = 0

mat = []
pts = []
n = 0


# trying to remember djikstra
def dj(start, togs, target):

    q = []
    hq.heappush(q, (0,start))
    dist = {}

    while q:
        cdist, state = hq.heappop(q)
        #print(state)

        if state in dist and cdist > dist[state]:
            continue


        if state == target:
            return cdist

        for tog in togs:
            new_state = apply(tog, state, target)
            if new_state is None:
                continue
            if new_state not in dist:
                dist[new_state] = cdist + 1
                hq.heappush(q, (cdist+1, new_state))
                continue
            if cdist+1 < dist[new_state]:
                dist[new_state] = cdist + 1
                hq.heappush(q, (cdist+1, new_state))


def apply(tog, state, target):
    new_state = []
    for i in range(len(state)):
        if i in tog:
            new_state.append(state[i]+1)
        else:
            new_state.append(state[i])
        if new_state[i] > target[i]:
            return None
    return tuple(new_state)



with open("input.txt", "r") as f:
    for i, line in enumerate(f.readlines()):

        ix1 = line.index("]")

        ix2 = line.index("{")
        toggles = line[ix1+2:ix2-1]

        target = line[ix2+1: len(line)-2]

        target = eval(f"({target})")
        toggles = toggles.split(" ")
        togs = []
        for tog in toggles:
            #print(toggles)
            tup = eval(tog)
            if isinstance(tup, int):
                tup = (tup,)
            togs.append(tup)

        start = tuple([0] * len(target))
        dist = {}
        print(f"solving {i}")
        best = dj(start, togs, target)

        ans+=best


print(ans)

