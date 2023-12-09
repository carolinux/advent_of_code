s = 0
with open("aoc1.txt", 'r') as f:
    for line in f.readlines():
        first = None
        last = None
        for ch in line:
            if ch.isdigit():
                if first is None:
                    first = int(ch)
                last = int(ch)

        s += first*10 + last


print(s)