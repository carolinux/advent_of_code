
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

ix = 0
for j, (lo,hi) in enumerate(seedz):
    for seed in range(lo, hi+1):
        ix+=1
        initial = seed
        if ix % 1000000 == 0:
            print(f"{seed*1.0 / (hi) } % done of the range {lo} - {hi}, {seed} out of {hi-lo}, {hi-seed} left")
        for i,m in enumerate(maps):
            found = False
            for dst, src, rang in m:
                if seed >= src and seed <= src + rang - 1:
                    # new value
                    seed = dst + abs(src-seed)
                    found = True
                    break
            #print(f"new value = {seed}")
            # if not found, seed stays this way
        # after doing all teh maps
        #print(f"Location for initial={initial} = {seed}")
        mbest = min(seed, mbest)

print(mbest)


