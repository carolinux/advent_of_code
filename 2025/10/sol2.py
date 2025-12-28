import sys
import math
import re
from collections import defaultdict, Counter
from operator import add, mul
import heapq as hq
from datetime import datetime as dt
import functools as ft
ans = 0

mat = []
pts = []
n = 0


def apply(state, ix, togs, last, target, times):
    new_state = []
    tog = togs[ix]


    for i in range(len(state)):
        if i in tog:
            new_state.append(state[i]+times)
        else:
            new_state.append(state[i])
        if new_state[i] > target[i]:
            return None, False
        if new_state[i] < target[i] and last[i]<=ix:
            return None, True
    return tuple(new_state), True



def dpsolve(start, target, togs):

    #print(target)
    iters = max(target) + 1
    last = {}
    for i in range(len(togs)):
        for num in togs[i]:
            last[num] = i


    @ft.lru_cache(maxsize=15000000)
    def recur(i, curr):
        #print(f"{curr} vs {target}")
        if curr == target:
            return 0
        if i >= len(togs):
            return math.inf
        minans = math.inf
        for j in range(iters):
            new_state, cont = apply(curr, i, togs, last, target, j)
            if cont is False:
                break
            if new_state is None:
                continue
            cand = recur(i+1, new_state) + j
            minans = min(cand, minans)

        return minans

    return recur(0, start)

maxx = 0
maxb = 0
with open("out2.txt", "w") as w:
    with open("input.txt", "r") as f:
        for i, line in enumerate(f.readlines()):
            #if i !=50:
            #    continue
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
            cnts.sort(key=lambda x: (x[0], target[x[1]-1])) # get smaller number of occurences first, break ties by favoring smaller overall count
            maxx = max(max(target), maxx)

            bytes_needed = len(target) * int(math.ceil(math.log2(max(target))))
            maxb = max(bytes_needed, maxb)
            #togs.sort(key=lambda x: len(x))

            togs2 = []
            for c, v in cnts:
                print(f"first putting the {c} that have value={v}")
                for tog in togs:
                    if v in tog and (tog not in togs2):
                        togs2.append(tog)
                        #print(togs2)

            togs = togs2
            #print(togs)
            togs = [set(x) for x in togs]
            print(f"{cnts[0][0]} out oof {len(target)} foor tc {i+1}, {target}, {togs}")
            #continue
            #sys.exit(0)
            #continue

            start = tuple([0] * len(target))
            dist = {}
            print(f"solving {i+1} - {target}")

            #continue
            #togs.sort(key=lambda x:len(x))t
            time1 = dt.now()
            best = dpsolve(start, target, togs)
            time2 = dt.now()
            print(best)
            print(time2-time1)
            w.write(f"{i+1},{best},{time2-time1}\n")
            w.flush()

            ans+=best
            #break


print(ans)
#print(maxx)
#print(maxb)
# solution: 18105
