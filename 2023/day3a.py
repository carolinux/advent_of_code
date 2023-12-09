mat = []

with open("aoc3.txt", 'r') as f:
    i = 1
    for line in f.readlines():

        line = line.strip()
        mat.append(line)

rows = len(mat)
s = 0
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
        found = False
        for k in range(fi, la):
            # check up, down, left, right, diag
            #if found:
            #    break

            for di, dj in [(0,1),(1,0),(-1, 0), (0, -1), (1, 1), (-1,-1), (1,-1), (-1,1)]:
                ci = i + di
                cj = k + dj

                if ci<0 or cj<0 or ci>= rows or cj>=n:
                    continue
                ch2 = mat[ci][cj]
                if not ch2.isdigit() and ch2 !='.':
                    found = True

        if found:
            s+=num


print(s)