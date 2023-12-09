
maps = []
currmap = []
with open("day5.txt", 'r') as f:

    for line in f.readlines():
        if 'seeds' in line:
            seeds = list(map(int, line.split(":")[1].split()))
            continue
        if line.strip() == '':
            if currmap:
                maps.append(currmap)
            currmap = []
            continue
        if 'map' in line:
            continue

        currmap.append(list(map(int, line.split())))

if currmap:
    maps.append(currmap)

seedz = []

for i in range(0, len(seeds), 2):
    st = seeds[i]
    rang = seeds[i+1]
    seedz.append((st, st+rang-1))


import math
mbest = math.inf


def overlap(x1, y1, x2, y2):
    if y1 < x2 or x1 > y2:
        return None
    return max(x1, x2), min(y1, y2)


def process(mi, ma):

    q = [(mi, ma)]

    for i, m in enumerate(maps):
        print(f"We are in map {i} out of {len(maps)}")

        if i>0:
            # q = nq
            nq.sort(key=lambda x: (x[0], -x[1]))
            q = []
            prevma = -1
            for mi, ma in nq:
                if ma <= prevma:
                    continue
                q.append((mi, ma))
                prevma = ma

            print(f"Queue size now : {len(q)}")

        nq = []

        while q:
            mi, ma = q.pop()
            matches = False
            for dst, src, rang in m:
                lo = src; hi = src+rang-1
                #print(f"mapped {lo} {hi} vs existing {mi, ma}")
                if overlap(mi, ma, lo, hi):
                    matches = True
                    mii, maa = overlap(mi, ma, lo, hi)
                    #print(f"{mi}, {ma} overlaps {lo}, {hi} (dst={dst}) with overlap = {mii, maa}, underlap={und}")
                    #ranges[i].discard((mi, ma))
                    mii = dst + abs(lo-mii)
                    maa = dst + abs(lo-maa)
                    nq.append((mii, maa))
                    #print(f"new_ranges: {nq}, curr: {q}")
                else:
                    #print(f"{mi} {ma} does not overlap {lo} {hi}")
                    pass
            if not matches:
                nq.append((mi, ma))

    #print(f"status: {nq}, {q}")
    res = min(x for x,y in nq + q)
    #print(res)
    return res



mbest = math.inf
for mi, ma in seedz:
    print(f"Processing {mi} {ma}")
    seed = process(mi, ma)
    mbest = min(seed, mbest)

print(mbest)


