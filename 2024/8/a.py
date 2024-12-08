import sys
import math
from collections import defaultdict
T = 50
#T = 10
#T=12


m = []
for _ in range(T):
    row = list(input().strip())
    m.append(row)

# create a map of positions
pos = defaultdict(list)
for i in range(len(m)):
    for j in range(len(m[0])):
        if m[i][j]!='.':
            pos[m[i][j]].append((i, j))

nodes = set()

def getd(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    #return abs(x2-x1) + abs(y2-y1)
    dx = x2-x1
    dy =y2-y1
    return math.sqrt(dx*dx + dy*dy)


def process(pos1, pos2, nodes, m):
    #print(pos1, pos2)
    x1, y1 = pos1
    x2, y2 = pos2
    for i in range(len(m)):
        for j in range(len(m[0])):

            dx1 = i - x1
            dx2 = i - x2
            dy1 = j - y1
            dy2 = j - y2
            if (dx1 == 2 * dx2 and dy1 == 2 *dy2) or  (dx2 == 2 * dx1 and dy2 == 2 *dy1) :
                nodes.add((i, j))
                m[i][j] = "#" # str(cnt) #f"{cnt}_{dist1}_{dist2}"
                #m[x1][y1] = "X"
                #m[x2][y2] = "X"

                #print(f"Found for {pos1} {pos2}: {i+1, j+1}")
                #for row in m:
                #    print(''.join(row))
                #m[i][j] = '.'
                #m[x1][y1] = "0"
                #m[x2][y2] = "0"
                #print("=========================")


for ant in pos:
    #print(pos[ant])
    for i in range(len(pos[ant])):
        for j in range(i+1, len(pos[ant])):
            if i == j:
                continue
            process(pos[ant][i], pos[ant][j], nodes, m)

print("===================")
for row in m:
    print(''.join(row))


#print(pos)


print(len(nodes))

