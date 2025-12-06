import sys
from collections import defaultdict
ans = 0
mat = []
with open("input.txt", "r") as f:
    for line in f.readlines():
        line = line.strip()
        row = list(line)
        mat.append(row)


ro = len(mat)
co = len(mat[0])
ans = 0

for i in range(ro):
    for j in range(co):
        ch = mat[i][j]
        if ch!='@':
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
        if cnt<4:
            ans+=1


print(ans)
