
import sys

fn = sys.argv[1]
fnw = sys.argv[2]

with open(fnw, 'w') as fw:
    with open(fn, 'r') as f:
        for line in f:
            line = line.strip()
            parts = line.split(":")
            name = parts[0].strip()
            comps = parts[1].strip().split(" ")
            if len(comps)==1:
                leaf = True
            else:
                leaf = False
            if not leaf:
                op1 = comps[0]
                op = comps[1]
                op2 = comps[2]


            if leaf:
                fw.write(f"{name} leaf {comps[0]}\n")
            else:
                fw.write(f"{name} nonleaf {op1} {op} {op2}\n")

