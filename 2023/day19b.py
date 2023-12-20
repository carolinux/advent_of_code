import sys

s = 0
mat = []
fn = 'day19.txt'
#fn = 'small.txt'

curr = (0, 0)

instr = True

inputs = []
workflows = {}

from dataclasses import dataclass
import re
import inspect

def mk_func(descr):

    elem = descr[0]
    comp = descr[1]
    val = int(descr[2:])

    assert comp == '>' or comp == '<'

    def f(part):
        if comp == '>':
            #get attribute x of part
            mi, mx = getattr(part, elem)
            # matching is the one bigger
            if mx <= val:
                return None, part
            if mi > val:
                return part, None
            else:
                part1 = part.copy()
                part2 = part.copy()

                setattr(part1, elem, (val+1, mx))
                setattr(part2, elem, (mi, val))

                return part1, part2

        else:
            #get attribute x of part
            mi, mx = getattr(part, elem)
            # matching is the one smaller
            if mi >= val:
                return None, part
            if mx < val:
                return part, None
            else:
                part1 = part.copy()
                part2 = part.copy()

                setattr(part1, elem, (mi, val-1))
                setattr(part2, elem, (val, mx))

                return part1, part2

    return f

import copy


@dataclass
class Part:

    def copy(self):
        return copy.deepcopy(self)

    def __repr__(self):
        return f"x={self.x}, m={self.m}, a={self.a}, s={self.s}"

    def __init__(self, x=None, m=None, a=None, s=None):
        if x is None:
            self.x = [1, 4000]
        else:
            self.x = x

        if m is None:
            self.m = [1, 4000]
        else:
            self.m = m

        if a is None:
            self.a = [1, 4000]
        else:
            self.a = a

        if s is None:
            self.s = [1, 4000]
        else:
            self.s = s


    def combos(self) -> int:
        res = 1
        #print(f"Combos of {self}")
        for x in [self.x, self.m, self.a, self.s]:
            res *= x[1] - x[0] + 1
        return res



@dataclass
class Workflow:

    def __init__(self, line):
        self.line = line
        self.id = self.line.split("{")[0]
        comps = re.match(".*{(.*)}", line)
        comps = comps.group(1).split(",")
        self.n = len(comps)
        self.res = [comp.split(":")[1] for comp in comps[:-1]] + [comps[-1]]
        self.func = [mk_func(comp.split(":")[0]) for comp in comps[:-1]]



    def process(self, part) -> str:

        new_wf_parts = []
        for i in range(self.n-1):
            st = self.res[i]
            matching, not_matching = self.func[i](part)
            if matching is not None:
                new_wf_parts.append((st, matching))
            part = not_matching

        # anything not rejected and not matched by any rule, is handled by the last rule
        st = self.res[-1]
        if part is not None:
            new_wf_parts.append((st, part))

        #print(f"After applying {self.line}, we have {new_wf_parts}")
        return new_wf_parts



def parse_input(line) -> dict:
    res = {}
    for x in 'xmas':
        m = re.match(".*" + x + "=(\d+),*}*", line)
        val = int(m.group(1))
        res[x] = val
    return res


def ssum(inp_dict) -> int:
    return sum([v for k,v in inp_dict.items()])

with open(fn, 'r') as f:

    for i,line in enumerate(f.readlines()):
        line = line.strip()
        if line == '':
            instr = False
            continue

        if instr:
            print("Parsing intructions")
            # parse instructions
            wf = Workflow(line)
            workflows[wf.id] = wf


final = []
q = [('in', Part())]
while True:

    nq = []
    for wfid, part in q:
        wf = workflows[wfid]
        additions = wf.process(part)
        for st, part in additions:
            if st == 'A':
                final.append(part)
                continue
            if st == 'R':
                continue

            nq.append((st, part))

    # finished
    q = nq
    if not q:
        break


ans = sum([p.combos() for p in final])
print(ans)


