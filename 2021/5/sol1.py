import sys
fn = "input.txt"



ans = 0
maxx = 0
maxy = 0
mat = []
arrows = []
with open(fn, 'r') as f:
    for line in f.readlines():
        parts =line.strip().split(" -> ")
        x1,y1 = parts[0].split(",")
        x2,y2 = parts[1].split(",")
        x1=int(x1);x2=int(x2);y2=int(y2);y1=int(y1)
        if x1 == x2:
            y1,y2 = min(y1,y2), max(y1, y2)
            arrows.append((x1,y1,x2,y2))
        elif y1 == y2:
            x1,x2 = min(x1,x2), max(x1, x2)
            arrows.append((x1,y1,x2,y2))

        maxx=max(maxx, x1, x2)
        maxy = max(maxy, y1, y2)

# rows = y
# cols = x

mat = [[0 for _ in range(maxx+1)] for _ in range(maxy+1)]
#print(mat)
ans = 0
for x1,y1,x2,y2 in arrows:
    for row in range(y1, y2+1):
        for col in range(x1, x2+1):
            if mat[row][col] == 1:
                ans+=1
            mat[row][col]+=1

print(ans)





