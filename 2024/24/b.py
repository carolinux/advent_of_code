import sys
from collections import defaultdict, namedtuple, deque
import os

OP = namedtuple("OP", "left right op res")

styles = {"AND": "style=solid", "XOR": "color=red; style=dotted", "OR": "style=dashed"}

def generate_graphviz_dot(graph) -> str:

    dot = ["digraph G {"]

    # Add the root node explicitly
    dot.append("    1 [shape=circle, style=bold];")

    # Add edges to the DOT graph
    sorted_keys = sorted(graph.keys())
    for node in sorted_keys:
        neighbors = graph[node]
        for neigh, op in neighbors:
            styl = styles[op]
            dot.append(f"    {node} -> {neigh}[{styl}];")
    dot.append("}")

    return "\n".join(dot)


def parse(input_string):
    # Split input into lines
    lines = list(input_string.strip().splitlines())
    g = defaultdict(list)
    rg = {}

    variables = {}
    ops = {}
    indeg = {}
    namemap = {}

    # Parse input lines
    for it in (1, 2, 3):
        for line in lines:
            if ":" in line and it == 1:
                # Parse variable assignments (e.g., x00: 1)
                var, value = line.split(":")
                variables[var.strip()] = int(value.strip())
            elif "->" in line:
                # Parse operations (e.g., x00 AND y00 -> z00)
                parts = line.split()
                left = parts[0]
                op = parts[1]
                right = parts[2]
                if right < left:
                    left, right = right, left
                result = parts[4]
                if left[0] == 'x' and right[0] == 'y':
                    assert op in ("AND", "XOR")
                    bit = left[1:]
                    namemap[result] = f"bit{bit}_{op}1"


                if it == 2:
                    result = namemap.get(result, result)
                    left = namemap.get(left, left)
                    right = namemap.get(right, right)


                    if "XOR1" in left and op  == "AND":
                        namemap[result] = left[:-4] +'AND2'

                    if "XOR1" in right and op  == "AND":
                        namemap[result] = right[:-4] +'AND2'

                    if "AND1" in right and op  == "OR":
                        namemap[result] = right[:-4] +'CARRY'

                    if "AND1" in left and op  == "OR":
                        namemap[result] = left[:-4] +'CARRY'

                    #if "XOR1" in left and op  == "AND":
                    #    namemap[result] = left[:-4] +'AND2'

                    #if "XOR1" in right and op  == "XOR":
                    #    namemap[result] = right[:-4] +'AND2'

                if it == 3:
                    result = namemap.get(result, result)
                    left = namemap.get(left, left)
                    right = namemap.get(right, right)
                    ops[result] = OP(left, right, op, result)
                    g[left].append(result)
                    g[right].append(result)
                    indeg[result] = 2

                    rg[result] = ops[result]


    return variables, ops, g, indeg, rg, namemap


input_data = sys.stdin.read()

vars, ops, g, indeg, rg, namemap = parse(input_data)
print(rg.keys())
for key in rg:
    if key[0] == 'z' and key !='z45':
        print(f"checking {key}")
        if rg[key].op != 'XOR':
            print(f"bad prev gates for {key}")


for key in rg:
    if "CARRY" in key:
        #print(f"checking {key}")
        #print(f"{rg[key].left} {rg[key].right}")
        bad_prefix = rg[key].left[:9] != rg[key].right[:9]
        if not (("AND1" in rg[key].left and "AND2" in rg[key].right) or ("AND2" in rg[key].left and "AND1" in rg[key].right)) or (bad_prefix):
            print(f"{key} bad, {rg[key]}")

    if "AND2" in key:
        bad_prefix = False
        if not (("CARRY" in rg[key].left and "XOR1" in rg[key].right) or ("XOR1" in rg[key].left and "CARRY" in rg[key].right)) or (bad_prefix):
            print(f"{key} bad, {rg[key]}")



res = ['z16', 'hmk', 'fcd', 'z33', 'z20', 'fhp']

for key, val in namemap.items():
    if val == "bit27_XOR1" or val == "bit27_AND1" or val == "bit20_XOR2":
        print(f"{val} {key}")
        res.append(key)

res.sort()

print(','.join(res))
#assert len(res) == 8



#sys.exit(0)

zq = deque()

xs = list(vars.keys())
xs = [x for x in xs if x[0]=='x']
xs.sort()
ys = list(vars.keys())
ys = [x for x in ys if x[0]=='y']
ys.sort()
assert len(ys) + len(xs) == len(vars)
assert len(ys) == len(xs)

keys_sorted = []
for x,y in zip(xs, ys):
    keys_sorted.append(x)
    keys_sorted.append(y)

for varname in keys_sorted:
    varvalue = vars[varname]
    zq.append((varname, varvalue))

end = {}
pg = defaultdict(list)
it = 0
while zq:
    it+=1
    varname, varvalue = zq.popleft()
    if varname[0] == 'z':
        end[varname] = varvalue

    for ch in g[varname]:

        indeg[ch]-=1
        op = ops[ch]
        pg[varname].append((ch, op.op))
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
            zq.appendleft((ch, val))
    text = generate_graphviz_dot(pg)
    dot = f"graphs/{it}.dot"
    png = f"graphs/{it}.png"
    with open(dot, "w") as file:
        file.write(text)
    os.system(f"dot -Tpng {dot} -o {png}")
    os.system(f"rm {dot}")


skeys = list(end.keys())
skeys.sort(reverse=True)
binstr = ''.join([str(end[k]) for k in skeys])
#rmprint(int(f"0b{binstr}", 2))

print(f"Num gates: {len(ops)}")
print(skeys)

