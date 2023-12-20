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

    def f(input_dict):
        if comp == '>':
            return input_dict[elem] > val
        else:
            return input_dict[elem] < val
    #print(inspect.getsource(f))
    return f



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



    def process(self, inp_dict) -> str:

        for i in range(self.n-1):
            if self.func[i](inp_dict):
                return self.res[i]

        return self.res[self.n-1]



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

        else:
            # parse inp
            inp = parse_input(line)
            inputs.append(inp)


#print(inputs)

for inp in inputs:
    curr = 'in'
    while True:
        wf = workflows[curr]
        next_state = wf.process(inp)
        if next_state == 'A':
            s+= ssum(inp)
            break
        elif next_state == 'R':
            break
        curr = next_state

print(s)
