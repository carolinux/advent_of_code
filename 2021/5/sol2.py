import sys
fn = "input.txt"
#fn="small.txt"


ans = 0
maxx = 0
maxy = 0
mat = []
arrows = []


def gdiff(x1,x2):
    if x1<x2:
        return 1
    if x1==x2:
        return 0
    return -1

with open(fn, 'r') as f:
    for line in f.readlines():
        parts =line.strip().split(" -> ")
        x1,y1 = parts[0].split(",")
        x2,y2 = parts[1].split(",")
        x1=int(x1);x2=int(x2);y2=int(y2);y1=int(y1)

        diffx = gdiff(x1,x2)
        diffy = gdiff(y1,y2)
        arrows.append(((x1,y1,x2,y2,diffx,diffy)))


        maxx=max(maxx, x1, x2)
        maxy = max(maxy, y1, y2)

# rows = y
# cols = x

mat = [[0 for _ in range(maxx+1)] for _ in range(maxy+1)]
#print(mat)
ans = 0
for x1,y1,x2,y2,dx,dy in arrows:
    row=y1;col=x1
    while True:
        if mat[row][col] == 1:
            ans+=1
        mat[row][col]+=1
        if row==y2 and col==x2:
            break
        row+=dy
        col+=dx

print(ans)

#print(arrows)





