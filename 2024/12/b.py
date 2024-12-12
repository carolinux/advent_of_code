from collections import defaultdict
n = 140

mat = []

for _ in range(n):
    row = list(input())
    mat.append(row)
#print(mat)

visited = set()


def explore(i, j, vis):
    vis.add((i, j))
    val = mat[i][j]
    for ch in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        x, y = i + ch[0], j + ch[1]
        if x >= 0 and x < n and y >= 0 and y < n and (x, y) not in vis:
            if mat[x][y] == val:
                explore(x, y, vis)

plots = {}
visited = set()
id = 0
for i in range(n):
    for j in range(n):
        if (i, j) in visited:
            continue
        vis = set()
        explore(i, j, vis)
        visited.update(vis)
        plots[id] = vis
        id += 1
ans = 0


def get_sides(cells, dir):
    a = list(cells)
    ans = 0
    if dir == (-1, 0) or dir == (1, 0):
        # these cells have no neighbors on top/bottom of them -> horizontal side
        d = defaultdict(list)
        for i, j in a:
            d[i].append(j)
        for i in d:
            d[i].sort()
    else:
        # these cells have no neighbors on top/bottom of them -> vertical side
        d = defaultdict(list)
        for i, j in a:
            d[j].append(i)
        for i in d:
            d[i].sort()

    for _, vals in d.items():
        sides = 1
        i = 1
        while i< len(vals):
            if vals[i] == vals[i-1] + 1:
                i+=1
                continue
            else:
                sides+=1
                i+=1

        ans+=sides


    return ans




for plot_id in plots:
    values = plots[plot_id]
    area = len(values)
    sides = 0
    for dir in (0, 1), (1, 0), (0, -1), (-1, 0):
        border = set()
        for i, j in values:

            if (i+dir[0], j+dir[1]) not in values:
                border.add((i, j))
        sides+= get_sides(border, dir)
    ans+=area*sides
    print(f"plot with value={mat[i][j]} has area={area} x sides={sides}")
print(ans)
