import sys
import math
from collections import defaultdict, Counter
from operator import add, mul
ans = 0



g = defaultdict(list)
with open("input.txt", "r") as f:
    for i, line in enumerate(f.readlines()):
        parts = line.strip().split(":")
        #print(parts[0])
        children = parts[1][1:].split()
        #print(children)
        g[parts[0]].extend(children)

def render_graph(graph: dict[str, list[str]], output_file: str = "graph.dot", highlight_nodes: set[str] = None):
    if highlight_nodes is None:
        highlight_nodes = set()

    with open(output_file, 'w') as f:
        f.write("digraph G {\n")
        f.write("  rankdir=LR;\n")
        f.write("  node [shape=box];\n")

        # Collect all nodes
        all_nodes = set(graph.keys())
        for neighbors in graph.values():
            all_nodes.update(neighbors)

        # Write highlighted nodes with styling
        for node in highlight_nodes:
            f.write(f'  "{node}" [style=filled, fillcolor=red, fontcolor=white];\n')

        # Write all edges
        for node, neighbors in graph.items():
            if not neighbors:
                f.write(f'  "{node}";\n')
            else:
                for neighbor in neighbors:
                    f.write(f'  "{node}" -> "{neighbor}";\n')

        f.write("}\n")
    print(f"DOT file written to {output_file}")
    print(f"Render with: dot -Tpng {output_file} -o graph.png")
    print(f"Or: dot -Tsvg {output_file} -o graph.svg")


def paths(node, targ, stop):
    if node in stop:
        return 0
    if node in targ:
        #if "fft" in vis and "dac" in vis:
        #    print("good found")
        return 1
        #return 0

    ans = 0

    for ch in g[node]:
        #if ch not in vis:
        #    vis.add(ch)
        ans+=paths(ch, targ, stop)
        #    vis.remove(ch)
    #print(f"partial ans {ans}")
    return ans

#render_graph(g, highlight_nodes={"dac", "fft"})
#sys.exit(0)
#ans = paths("svr", "out")
#print(ans)
# dac->fft = 0
# dac -> out = 6141
# svr-fft
# fft-dac
#sol1  = paths("fft", )
#print(sol1)
#sys.exit(0)


sol0 = paths("svr", {"fft"}, {"sjl", "tpb", "glj", "zuv"})
print(sol0)

sol1a  = paths("fft", {"ddt"}, {"ohq", "vca"})
print(sol1a)

sol1b  = paths("fft", {"ohq"}, {"ddt", "vca"})
print(sol1b)

sol1c  = paths("fft", {"vca"}, {"ddt", "ohq"})
print(sol1b)

sol2  = paths("ddt", {"dac"}, {"bhi", "you", "mpm", "jat", "qsg"})
print(sol2)

sol3  = paths("ohq", {"dac"}, {"bhi", "you", "mpm", "jat", "qsg"})
print(sol3)

sol4  = paths("vca", {"dac"}, {"bhi", "you", "mpm", "jat", "qsg"})
print(sol4)

sol5  = paths("dac", {"out"}, {})
print(sol5)

# from the visualization
p1 = sol0* sol1a * sol2 * sol5
p2 = sol0 * sol1b * sol3 * sol5
p3 = sol0 * sol1c * sol4 * sol5
print(p1+p2+p3)











