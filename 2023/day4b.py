from collections import defaultdict
mult = defaultdict(lambda: 1)
ix = 1
with open("aoc4.txt", 'r') as f:
    for line in f.readlines():
        to_find, cards = line.split("|")
        to_find = to_find.split(":")[1].strip()
        cards = cards.strip()
        to_find = set(to_find.split(" "))
        cards = set(cards.split(" "))
        incr = 0
        for w in to_find:
            try:
                int(w)
            except:
                continue
            if w in cards:
                incr+=1

        # card ix had incr matches
        for j in range(ix+1, ix+incr+1):
            mult[j] += mult[ix]
        if ix not in mult:
            mult[ix] = 1
        ix+=1

s = 0
for k, v in mult.items():
    s += v
print(s)