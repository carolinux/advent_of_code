import heapq as hq
from copy import copy
import sys

cha = 'dddb'
chb = 'ccbc'
chc = 'abad'
chd = 'baca'

# example

#cha = 'bdda'
#chb = 'ccbd'
#chc = 'bbac'
#chd = 'daca'


hallway = '.' * 11

# in hallway
targeti = {'a': 2, 'b': 4, 'c':6, 'd':8}
cost = {'a': 1 , 'b':10, 'c':100, 'd':1000}

# in chamb
ixes = {'a': [0,1,2,3], 'b':[4,5,6,7], 'c':[8,9,10,11], 'd': [12,13,14,15]}

halls = (0,1,3,5,7,9,10)
forbidden = (2,4,6,8)

def str2(li):
    return ''.join(li)

class State:
    def __init__(self, hallway, chamb):
        self.hallway = hallway
        self.chamb = chamb

    def __hash__(self):
        # to implement
        return hash(hash(self.hallway) + hash(self.chamb))


    def __str__(self):

        line1 = self.hallway
        #line1 = [ch if ch !='.' else '#' for ch in self.hallway ]
        #line1 = ''.join(line1)
        line2 = ('#'*2) + self.chamb[0] + "#" + self.chamb[4] + "#" + self.chamb[8] + "#" + self.chamb[12] + ('#'*2)
        line3 = ('#'*2) + self.chamb[1] + "#" + self.chamb[5] + "#" + self.chamb[9] + "#" + self.chamb[13] + ('#'*2)
        line4 = ('#'*2) + self.chamb[2] + "#" + self.chamb[6] + "#" + self.chamb[10] + "#" + self.chamb[14] + ('#'*2)
        line4 = ('#'*2) + self.chamb[3] + "#" + self.chamb[7] + "#" + self.chamb[11] + "#" + self.chamb[15] + ('#'*2)
        return "\n".join([11*"=", line1,line2,line3,11*"="])

    def __eq__(self, o):
        return self.hallway == o.hallway and self.chamb == o.chamb


    def __lt__(self, o):
        return 0


    def new_entry(self, ch, curri): # new entry from the hallway
        ix1, ix2, ix3, ix4 = ixes[ch]
        ch1 = self.chamb[ix1]
        ch2 = self.chamb[ix2]
        ch3 = self.chamb[ix3]
        ch4 = self.chamb[ix4]
        empty4 = ch1 == '.' and ch2 == '.' and ch3 == '.' and ch4 == '.'
        empty3 = ch1 == '.' and ch2 == '.' and ch3 == '.' and ch4 == ch
        empty2 = ch1 == '.' and ch2 == '.' and ch3 == ch and ch4 == ch
        empty1 = ch1 == '.' and ch2 == ch and ch3 == ch and ch4 == ch
        if not (empty4 or empty3 or empty2 or empty1):
            return None
        origi = curri
        #assert i !=2
        if curri <targeti[ch]:
            step = 1
        else:
            step = -1
        assert curri != targeti[ch]


        moves = 0
        while curri != targeti[ch]:
            curri+=step
            clear = self.hallway[curri] == '.'
            moves+=1
            if not clear:
                return None

        new_hallway = list(self.hallway)
        new_chamb = list(self.chamb)
        if empty1:
            moves+=1
            new_chamb[ix1] = ch
        elif empty2:
            moves+=2
            new_chamb[ix2] = ch
        elif empty3:
            moves+=3
            new_chamb[ix3] = ch
        else:
            new_chamb[ix4] = ch
            moves+=4
        score = cost[ch] * moves
        new_hallway[origi] = '.'
        new_state = State(str2(new_hallway), str2(new_chamb))
        return (score, new_state)


    def hallcheck(self):

        for i, ch in enumerate(self.hallway):
            if ch == '.':
                continue
            cand = self.new_entry(ch, i)
            if cand is not None:
                return [cand]
        return []

    def check(self, tch):
        cands = []
        ix1, ix2, ix3, ix4 = ixes[tch]
        ch1 = self.chamb[ix1]
        ch2 = self.chamb[ix2]
        ch3 = self.chamb[ix3]
        ch4 = self.chamb[ix4]
        if ch1 == tch and ch2 == tch and ch3 ==tch and ch4 ==tch:
            return [] # settled
        if ch1 == '.' and ch2 == '.' and ch3 =='.' and ch4 == '.':
            return [] # no exit possible
        if ch1 == '.' and ch2 == '.' and ch3 =='.' and ch4 == tch:
            return [] # settled

        if ch4 ==tch and ch3 ==tch and ch2 == tch and ch1 =='.':
            return []  # settled

        if ch4 ==tch and ch3 ==tch and ch2 == '.' and ch1 =='.':
            return []  # settled

        if ch4 ==tch and ch3 =='.' and ch2 == '.' and ch1 =='.':
            return []  # settled


        moves = 0
        new_chamb = list(self.chamb)
        if ch1 != '.':
            # move ch1
            ch = ch1
            moves+=1
            new_chamb[ix1] = '.'
        elif ch1 == '.' and ch2 != '.':
            # move ch2
            ch = ch2
            moves+=2
            new_chamb[ix2] = '.'

        elif  ch1 == '.' and ch2 == '.' and ch3 != '.':
            # move ch3
            ch = ch3
            moves+=3
            new_chamb[ix3] = '.'
        elif  ch1 == '.' and ch2 == '.' and ch3 == '.' and ch4 != '.':
            # move ch4
            ch = ch4
            moves+=4
            new_chamb[ix4] = '.'
        else:
            raise Exception(f"should not have reached here {self.chamb}, tch={tch}")


        new_chamb = str2(new_chamb)
        curri = targeti[tch]

        for i in range(curri+1, 11):
            if i in forbidden:
                continue
            if self.hallway[i] != '.':
                break
            score = cost[ch] * (moves + abs(i-curri))
            new_hallway = list(self.hallway)
            new_hallway[i] = ch
            new_state = State(str2(new_hallway), new_chamb)
            cands.append((score, new_state))

        for i in range(curri-1, -1, -1):
            if i in forbidden:
                continue
            if self.hallway[i] != '.':
                break
            score = cost[ch] * (moves + abs(i-curri))
            new_hallway = list(self.hallway)
            new_hallway[i] = ch
            new_state = State(str2(new_hallway), new_chamb)
            cands.append((score, new_state))


        return cands


    def is_final(self):
        return self.chamb == 'aaaabbbbccccdddd'



    def neighs(self):
        sc = []
        sc.extend(self.hallcheck())

        # can I move anything in the hallway inside a room?
        # if yes, return only that and only one
        if len(sc) > 0:
            return sc

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
print('start')
steps = 0
while q:

    score, state = hq.heappop(q)
    #print(score)
    #print(state)
    #input("prompt")
    final = state.is_final()
    if final:
        print(score)
        print(state)
        sys.exit(0)

    if dist[state] < score:
        continue

    for sc,st in state.neighs():
        sc= sc+score
        if st in dist and dist[st] <= sc:
            continue
        dist[st] = sc
        hq.heappush(q, (sc, st))
