designs = input().strip().split(',')
designs = [d.strip() for d in designs]
import functools as ft

@ft.lru_cache(maxsize=None)
def ways(towel, i):
    n = len(towel)
    if i == n:
        return 1

    cnt = 0
    for design in designs:
        if i + len(design)> n:
            continue
        match = True
        ix = 0
        for j in range(i, i+len(design)):
            if towel[j] != design[ix]:
                match = False
            ix+=1
        if not match:
            continue
        #print(f"choosing {design} for towel {towel} starting at {i} and now starting at {i+len(design)}")
        cnt+=ways(towel, i+len(design))

    return cnt

input()
towels = []
while True:
    try:
        line = input().strip()
    except EOFError:
        break
    if line == "":
        break
    towels.append(line)
#print(designs)
#print(towels)
ans = 0
for towel in towels:
    ans+=ways(towel, 0)

print(ans)

