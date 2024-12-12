
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
for plot_id in plots:
    values = plots[plot_id]
    area = len(values)
    perim = 0
    for i, j in values:
        # how many neighbours are there with different value
        # check i+1, j, i-1, j, i, j+1, i, j-1
        for dir in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            x, y = i + dir[0], j + dir[1]
            if (x, y) not in values:
                perim+=1
    #print(f"plot with value={mat[i][j]} has area={area} x perim={perim}")
    ans+=area*perim
print(ans)
