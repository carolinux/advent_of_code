s = 0

cands = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
# map of cands to digits
m = {}
for i in range(len(cands)):
    m[cands[i]] = i


with open("aoc1_small.txt", 'r') as f:
    for line in f.readlines():
        first = None
        last = None
        for i in range(len(line)):
            if line[i].isdigit():
                if first is None:
                    first = int(line[i])
                last = int(line[i])
                continue

            for cand in cands:
                wlen = len(cand)
                if line[i:i+wlen] == cand:
                    dig = m[line[i:i+wlen]]
                    if first is None:
                        first = dig
                    last = dig


        s += first*10 + last


print(s)