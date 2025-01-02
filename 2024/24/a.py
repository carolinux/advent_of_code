import sys
from collections import defaultdict, namedtuple, deque

OP = namedtuple("OP", "left right op res")

def parse(input_string):
    # Split input into lines
    lines = input_string.strip().splitlines()
    g = defaultdict(list)

    variables = {}
    ops = {}
    indeg = {}

    # Parse input lines
    for line in lines:
        if ":" in line:
            # Parse variable assignments (e.g., x00: 1)
            var, value = line.split(":")
            variables[var.strip()] = int(value.strip())
        elif "->" in line:
            # Parse operations (e.g., x00 AND y00 -> z00)
            parts = line.split()
            left = parts[0]
            op = parts[1]
            right = parts[2]
            result = parts[4]
            ops[result] = OP(left, right, op, result)
            g[left].append(result)
            g[right].append(result)
            indeg[result] = 2


    return variables, ops, g, indeg


input_data = sys.stdin.read()

vars, ops, g, indeg = parse(input_data)

zq = deque()

for varname, varvalue in vars.items():
    zq.append((varname, varvalue))

end = {}
while zq:
    varname, varvalue = zq.popleft()
    if varname[0] == 'z':
        end[varname] = varvalue

    for ch in g[varname]:
        indeg[ch]-=1
        if indeg[ch] == 0:
            op = ops[ch]
            left = vars[op.left]
            right = vars[op.right]
            if op.op == "AND":
                val = left & right
            elif op.op == "OR":
                val = left | right
            else:
                val = left ^ right
            vars[ch] = val
            zq.append((ch, val))


skeys = list(end.keys())
skeys.sort(reverse=True)
binstr = ''.join([str(end[k]) for k in skeys])
print(int(f"0b{binstr}", 2))

print(f"Num gates: {len(ops)}")

