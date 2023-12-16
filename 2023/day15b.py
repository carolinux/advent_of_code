
fn = 'day15.txt'


def haash(seg):
    res = 0
    for ch in seg:
        val = ord(ch)
        res+=val
        res*=17
        res = res % 256

    return res


class SlotMap:

    def __init__(self):
        self.slots = [Slot(i+1) for i in range(256)]

    def add(self, key, val):
        slot_id = haash(key)
        self.slots[slot_id].add_or_update(key, val)

    def remove(self, key):
        slot_id = haash(key)
        self.slots[slot_id].remove(key)

    def score(self):
        return sum(sl.score() for sl in self.slots)


class Slot:

    def __init__(self, mult):
        self.mult = mult
        self.keys = []
        self.values = []

    def index(self, key) -> bool:
        try:
            return self.keys.index(key)
        except ValueError:
            return -1

    def add_or_update(self, key, val):
        ix = self.index(key)
        if ix == -1:
            self.keys.append(key)
            self.values.append(val)
        else:
            self.values[ix] = val

    def remove(self, key):
        ix = self.index(key)
        if ix == -1:
            return
        self.keys.pop(ix)
        self.values.pop(ix)

    def score(self):
        s = 0
        for i in range(len(self.values)):
            s += self.mult * (i+1) * self.values[i]
        return s

mp = SlotMap()

with open(fn, 'r') as f:
    segs = f.readline().strip().split(",")
    #print(segs)
    for seg in segs:
        if "-" in seg:
            key = seg[:-1]
            mp.remove(key)
        else:
            key, val = seg.split("=")
            mp.add(key, int(val))



print(mp.score())
