import sys
from collections import defaultdict, deque
import copy
ans = 0
mat = []
with open("input.txt", "r") as f:
    for line in f.readlines():
        line = line.strip()
        row = list(line)
        mat.append(row)


ro = len(mat)
co = len(mat[0])
mat2 = copy.deepcopy(mat)
ans = 0
zq = deque()
visited = set()

for i in range(ro):
    for j in range(co):
        ch = mat[i][j]
        if ch!='@':
            mat2[i][j] = -1
            continue
        cnt = 0
        for diffi in (-1, 0, 1):
            for diffj in (-1, 0, 1):
                ii = i + diffi
                jj = j + diffj
                if ii ==i  and jj == j:
                    continue
                if ii >=ro or ii <0 or jj>=co or jj<0:
                    continue
                if mat[ii][jj] == '@':
                    cnt+=1

        mat2[i][j] = cnt
        if cnt<4:
            zq.append((i, j))
            visited.add((i, j))
            ans+=1



while zq:
    i, j = zq.popleft()
    # cleared the roll here
    for diffi in (-1, 0, 1):
        for diffj in (-1, 0, 1):
            ii = i + diffi
            jj = j + diffj
            if (ii, jj) in visited:
                continue
            if ii ==i  and jj == j:
                continue
            if ii >=ro or ii <0 or jj>=co or jj<0:
                continue
            if mat[ii][jj] != '@':
                continue

            mat2[ii][jj]-=1

            if mat2[ii][jj] < 4:
                zq.append((ii, jj))
                visited.add((ii, jj))
                ans+=1



print(mat2)




print(ans)
