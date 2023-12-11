
mat = []


with open("day11.txt", 'r') as f:


    # read the universe, expanding rows as we read
    for i,line in enumerate(f.readlines()):
        mat.append(list(line.strip()))
        if set(mat[-1]) == {'.'}:
            mat.append(mat[-1])


rows = len(mat)
cols = len(mat[0])
# expand cols:
to_expand = []
for j in range(cols):
    empty = True
    for i in range(rows):
        if mat[i][j] != '.':
            empty = False
            break
    if empty:
        to_expand.append(j)

if to_expand:
    #print(f"previous cols: {cols}")
    print(to_expand)
    to_expand = [-1] + to_expand
    for i in range(rows):
        new_row = []
        row = mat[i]



        for k in range(1, len(to_expand)):
            st = to_expand[k-1]+1
            end = to_expand[k]

            fragment = row[st:end] + ['.', '.']
            #print(f"fragment: {len(fragment)}")
            new_row.extend(fragment)

        # forgot about the last one here
        last_k = to_expand[-1]
        if last_k < len(row) - 1:
            new_row.extend(row[last_k+1:])
        #print(f"end row, {len(new_row)}")
        mat[i] = new_row


cols = len(mat[0])

print(f"Rows: {rows}, cols={cols}")

galaxies = []

for i in range(rows):
    for j in range(cols):
        if mat[i][j] == '#':
            galaxies.append((i, j))



s = 0
n = len(galaxies)

for i, (gi, gj) in enumerate(galaxies):

    for j in range(i+1, n):
        xi,xj = galaxies[j]
        dist = abs(gi-xi) + abs(gj-xj)
        s+=dist




print(s)





