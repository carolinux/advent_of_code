
from collections import Counter


class Card:
    def __init__(self, s, bid):
        self.s = s
        self.bid = bid
        self.cnt = Counter(s)
        self.counts = self.cnt.most_common()
        #print(self.counts)
        if self.counts[0][1] == 5:
            self.type = 5
        elif self.counts[0][1] == 4:
            self.type = 4
        elif self.counts[0][1] == 3 and self.counts[1][1] == 2:
            # full house
            self.type = 3.5
        elif self.counts[0][1] == 3 and self.counts[1][1] == 1:
            self.type = 3

        elif self.counts[0][1] == 2 and self.counts[1][1] == 2:
            self.type = 2.5

        elif self.counts[0][1] == 2 and self.counts[1][1] == 1:
            self.type = 2
        else:
            self.type = 1

    def lt(self, a, b):
        ix1 = '23456789TJQKA'.index(a)
        ix2 = '23456789TJQKA'.index(b)
        return ix1 < ix2

    def __lt__(self, other) -> bool:

        if self.type == other.type:

            for i in range(5):
                if self.s[i] == other.s[i]:
                    continue
                else:
                    return self.lt(self.s[i], other.s[i])
        else:
            return self.type < other.type


cards = []
se = set()
with open("aoc7.txt", 'r') as f:

    for line in f.readlines():
        card, bid = line.split()
        if card in se:
            raise Exception(f"duplicate card {card}.. did not expect this from the description")
        se.add(card)
        card = Card(card, int(bid))
        cards.append(card)

cards.sort()
s = 0
for i in range(len(cards)):
    rank = i+1
    #print(cards[i].s, cards[i].type, cards[i].bid, rank)
    s+= rank * cards[i].bid


print(s)


