s = 0
with open("aoc4.txt", 'r') as f:
    for line in f.readlines():
        wins, card = line.split("|")
        wins = wins.split(":")[1].strip()
        card = card.strip()
        #print(wins)
        #print(card)
        wins = set(wins.split(" "))
        card = set(card.split(" "))
        incr = 0
        #matches = False
        for w in wins:
            try:
                int(w)
            except:
                continue
            if w in card:
                #s += incr
                if incr == 0:
                    incr = 1
                else:
                    incr *= 2

        s += incr

print(s)