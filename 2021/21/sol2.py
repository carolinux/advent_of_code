
p1 = 10
p2 = 2


#p1 = 4
#p2 = 8


import functools as ft
from collections import Counter

SCORES = Counter()

for i in range(1,4):
    for j in range(1,4):
        for k in range(1, 4):
            s = i+j+k
            SCORES[s]+=1


@ft.lru_cache(maxsize=None)
def recur(scs, poss, t):

    wins = [0, 0]
    new_turn = 1-t

    for posincr, count in SCORES.items():

        new_pos = poss[t] + posincr
        if new_pos>10:
            new_pos%=10
        incr = new_pos

        if scs[t] + incr>=21:
            wins[t] +=count
            continue
        if t == 0:
            new_scores = (scs[0]+incr, scs[1])
            new_poss = (new_pos, poss[1])
        else:
            new_scores = (scs[0], scs[1]+incr)
            new_poss = (poss[0], new_pos)

        wins2 = recur(new_scores, new_poss, new_turn)
        wins[0]+=wins2[0]*count
        wins[1]+=wins2[1]*count

    return wins

wins = recur((0, 0), (p1,p2), 0)
print(wins)
print(max(wins))
