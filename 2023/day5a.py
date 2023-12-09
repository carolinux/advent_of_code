
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



import math
mbest = math.inf

for seed in seeds:
    for m in maps:
        found = False
        for dst, src, rang in m:
            if seed >= src and seed <= src + rang - 1:
                # new value
                seed = dst + abs(src-seed)
                found = True
                break
        # if not found, seed stays this way
    # after doing all teh maps
    mbest = min(seed, mbest)

print(mbest)


