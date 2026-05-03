import heapq as hq
from copy import copy
import sys

cha = 'db'
chb = 'cc'
chc = 'ad'
chd = 'ba'

# example

cha = 'ba'
chb = 'cd'
chc = 'bc'
chd = 'da'


hallway = '.' * 11

# in hallway
targeti = {'a': 2, 'b': 4, 'c':6, 'd':8}
cost = {'a': 1 , 'b':10, 'c':100, 'd':1000}

# in chamb
ixes = {'a': [0,1], 'b':[2,3], 'c':[4,5], 'd': [6,7]}

halls = (0,1,3,5,7,9,10)
forbidden = (2,4,6,8)

class State:
    def __init__(self, hallway, chamb):
        self.hallway = hallway
        self.chamb = chamb

    def __hash__(self):
        # to implement
        return hash(hash(self.hallway) + hash(self.chamb))


    def __eq__(self, o):
        return self.hallway == o.hallway and self.chamb == o.chamb


    def new_entry(self, ch, curri):
        ix1, ix2 = ixes[ch]
        ch1 = self.chamb[ix1]
        ch2 = self.chamb[ix2]
        empty = ch1 == '.' and ch2 == '.'
        halfempty = ch1 == '.' and ch2 == ch
        if not (empty or halfempty):
            return None
        origi = curri
        #assert i !=2
        if curri <targeti[ch]:
            step = 1
        else:
            step = -1


        moves = 0
        while curri != targeti[ch]:
            curri+=step
            clear = self.hallway[curri] == '.'
            moves+=1
            if not clear:
                return None

        new_hallway = copy(self.hallway)
        new_chamb = copy(self.chamb)
        if halfempty:
            moves+=1
            new_chamb[ix1] = ch
        else:
            new_chamb[ix2] = ch
            moves+=2
        score = cost[ch] * moves
        new_hallway[origi] = '.'
        new_state = State(new_hallway, new_chamb)
        return (score, new_state)


    def hallcheck(self):

        for i, ch in enumerate(self.hallway):
            if ch == '.':
                continue
            cand = self.new_entry(ch, i)
            if cand is not None:
                return [cand]
        return []

    def check(self, ch):
        cands = []
        ix1, ix2 = ixes[ch]
        ch1 = self.chamb[ix1]
        ch2 = self.chamb[ix2]
        if ch1 == ch and ch2 == ch:
            return [] # settled
        moves = 0
        new_chamb = copy(self.chamb)
        if ch1 == '.':
            # move ch2
            moves+=2
            new_chamb[ix2] = '.'

        else:
            # move ch1
            moves+=1
            new_chamb[ix1] = '.'


        curri = targeti[ch]

        for i in range(curri+1, 11):
            if i in forbidden or self.hallway[i] !='.':
                continue
            score = cost[ch] * (moves + abs(i-curri))
            new_hallway = copy(self.hallway)
            new_hallway[i] = ch
            new_state = State(new_hallway, new_chamb)
            cands.append((score, new_state))

        for i in range(curri-1, -1, -1):
            if i in forbidden or self.hallway[i] !='.':
                continue
            score = cost[ch] * (moves + abs(i-curri))
            new_hallway = copy(self.hallway)
            new_hallway[i] = ch
            new_state = State(new_hallway, new_chamb)
            cands.append((score, new_state))


        return cands


    def is_final(self):
        return self.chamb == 'aabbccdd'



    def neighs(self):
        sc = []
        sc.extend(self.hallcheck())

        # can I move anything in the hallway inside a room?
        # if yes, return only that and only one
        if len(sc) > 0:
            return sc[0]

        # otherwise, look into exit moves
        sc.extend(self.check('a'))
        sc.extend(self.check('b'))
        sc.extend(self.check('c'))
        sc.extend(self.check('d'))
        return sc





q = []
state = State(hallway, cha+chb+chc+chd)
hq.heappush(q, (0, state))
dist = {}
dist[state] = 0

while q:

    score, state = hq.heappop(q)
    final = state.is_final()
    if final:
        print(score)
        sys.exit(0)

    if dist[state] < score:
        continue

    for sc,st in state.neighs():
        if st in dist and dist[st] <= sc:
            continue
        dist[st] = sc
        hq.heappush(q, (sc, st))
