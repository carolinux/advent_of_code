import sys
from collections import Counter
import itertools as it
import copy
fn = "input.txt"
#fn = "small.txt"


mp = {2:[1], 3:[7], 4:[4], 5:[2,3,5], 6: [6,0,9], 7:[8]}

wires ={
    0: 'abcefg',
    1 :'cf',
    2: "acdeg",
    3: "acdfg",
    4: "bcdf",
    5: "abdfg",
    6: "abdefg",
    7: "acf",
    8: "abcdefg",
    9: "abcdfg"

}


rwires ={
    'abcefg':0,
    'cf':1,
    "acdeg":2,
    "acdfg":3,
    "bcdf":4,
    "abdfg":5,
    "abdefg":6,
    "acf":7,
    "abcdefg":8,
    "abcdfg":9

}


"""
  0:      1:      2:      3:      4:
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....


 5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg
"""


def verificat(final_mapping, outs):
    if len(final_mapping) == 6:
        ks = set();vals = set();
        for key, val in final_mapping.items():
            ks.add(key)
            vals.add(val)

        for k in 'abcdefg':
            if k not in ks:
                for val in 'abcdefg':
                    if val not in vals:
                        final_mapping[k] = val

    nums = []
    for out in outs:
        out2 = []
        for ch in out:
            out2.append(final_mapping[ch])
        out2.sort()
        outstr = "".join([str(x) for x in out2])
        print(outstr)
        try:
            num = rwires[outstr]
            nums.append(num)
        except:
            return []


    return nums



# overkill, could have done 7! exhaustive search of the mappings
def solve(ins, outs):
    ins.sort(key=lambda x: len(x))


    def recur(ix, mapping):
        if ix == len(ins):
            return mapping
        if len(mapping)>=6:
            nums = verificat(mapping, outs)
            if len(nums) == 0:
                return None
            return mapping
        curr = ins[ix]
        source = list(curr)
        lc = len(curr)
        if lc == 7:
            return recur(ix+1, mapping)
        opts = mp[lc]
        for opt in opts:
            ws = wires[opt]
            assert len(ws) == len(curr)
            for targ in it.permutations(ws):
                good = 1
                new_mapping = copy.copy(mapping)
                for ch1,ch2 in zip(source, targ):
                    if ch1 in mapping and mapping[ch1] !=ch2:
                        good = 0
                        break
                    new_mapping[ch1] = ch2

                vals = set()
                for _, v in new_mapping.items():
                    if v in vals:
                        good = 0
                        break
                    vals.add(v)

                if good:
                    final_mapping = recur(ix+1, new_mapping)
                    if final_mapping is not None:
                        return final_mapping
        return None

    final_mapping = recur(0, {})
    assert final_mapping is not None
    nums = verificat(final_mapping, outs)
    return nums[0]*1000 + nums[1] * 100 + nums[2] * 10 + nums[3]

ans = 0

with open(fn, "r") as f:
    for line in f.readlines():
        if line.strip() == "":
            continue
        print(f"line:{line}xxx")
        parts = line.strip().split(" | ")
        ins = parts[0].split(" ")
        outs = parts[1].split(" ")
        ans+=solve(ins, outs)

#print(outs)
print(ans)
