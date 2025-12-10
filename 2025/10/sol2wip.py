import sys
import math
import re
from collections import defaultdict, Counter
from operator import add, mul
import heapq as hq
import functools as ft
ans = 0

mat = []
pts = []
n = 0


def apply(state, i, togs, target, times):
    new_state = []
    tog = togs[i]

    have_more = [False] * len(state)
    for j in range(i+1, len(togs)):
        for ix in togs[j]:
            have_more[ix] = True

    for i in range(len(state)):
        if i in tog:
            new_state.append(state[i]+times)
        else:
            new_state.append(state[i])
        if new_state[i] > target[i]:
            return None
        if new_state[i] < target[i] and not have_more[i]:
            return None
    return tuple(new_state)



def dpsolve(start, target, togs):

    #print(target)
    iters = max(target) + 1


    @ft.lru_cache(maxsize=None)
    def recur(i, curr):
        #print(f"{curr} vs {target}")
        if curr == target:
            return 0
        if i >= len(togs):
            return math.inf
        minans = math.inf
        for j in range(iters):
            new_state = apply(curr, i, togs, target, j)
            if new_state is None:
                continue
            cand = recur(i+1, new_state) + j
            minans = min(cand, minans)

        return minans

    return recur(0, start)


with open("input.txt", "r") as f:
    for i, line in enumerate(f.readlines()):
        ix1 = line.index("]")

        ix2 = line.index("{")
        toggles = line[ix1+2:ix2-1]

        target = line[ix2+1: len(line)-2]

        target = eval(f"({target})")
        toggles = toggles.split(" ")
        togs = []
        cnt = Counter()
        for tog in toggles:
            #print(toggles)
            tup = eval(tog)
            if isinstance(tup, int):
                tup = (tup,)
            togs.append(tup)
            for num in tup:
                cnt[num]+=1

        #print(f"{len(target)}: {cnt}")
        cnts = [(v, k) for k,v in cnt.items()]
        cnts.sort()

        togs.sort(key=lambda x: -len(x))

        togs2 = []
        for c, v in cnts:
            print(f"first putting the {c} that have value={v}")
            for tog in togs:
                if v in tog and (tog not in togs2):
                    togs2.append(tog)
                    #print(togs2)

        togs = []
        print(togs)

        for tog in togs2:
            a = []
            for j in range(len(target)):
                if j in tog:
                    a.append(1)
                else:
                    a.append(0)

            togs.append(tuple(a))

        #continue

        start = tuple([0] * len(target))
        dist = {}
        print(f"solving {i}")
        #togs.sort(key=lambda x:-len(x))
        best = dpsolve(start, target, togs)
        print(best)

        ans+=best
        #break


print(ans)

