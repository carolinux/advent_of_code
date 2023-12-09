mat = []
with open("aoc3.txt", 'r') as f:
    i = 1
    for line in f.readlines():
        line = line.strip()
        mat.append(line)

rows = len(mat)
s = 0
ix = 0
entries = {}
m = {}
for i in range(rows):
    j = 0
    n = len(mat[i])
    while j <n:
        ch = mat[i][j]
        if not ch.isdigit():
            j+=1
            continue
        fi = j
        num = 0
        while ch.isdigit():

            num = (num * 10) + int(ch)
            j+=1
            if j == n:
                break
            ch = mat[i][j]
        la = j
        # we found a number
        m[ix] = num
        for k in range(fi, la):
           entries[(i, k)] = ix
        ix += 1

for i in range(rows):
    n = len(mat[i])
    for j in range(n):
        if mat[i][j] != '*':
            continue
        # find adjacent numbers
        adjs = set() # the indices
        for di, dj in [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
            ci = i + di
            cj = j + dj
            if ci < 0 or cj < 0 or ci >= rows or cj >= n:
                continue
            if (ci, cj) in entries:
                adjs.add(entries[(ci, cj)])
        if len(adjs) == 2:
            ix1 = adjs.pop()
            ix2 = adjs.pop()
            s += m[ix1] * m[ix2]

print(s)