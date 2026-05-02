

ax = (185, 221)
ay = (-122, -74)
M = 10000

ax = (20, 30)
ay =(-10, -5)
M = 1000


xbounds = (1, 30)

def simulat(vx, vy):
    x,y=(0,0)
    mx = 0
    while True:
        x+=vx
        y+=vy

        vy-=1
        if vx>0:
            vx-=1
        elif vx<0:
            vx+=1
        mx = max(mx, y)
        if x>ax[1] or y<ay[0]:
            return True, -1

        if ax[0]<=x<=ax[1] and ay[0]<=y<=ay[1]:
            return False, mx

    raise Exception("should not reach here")




def bsearch(x):
    l = 0
    r = M
    curr_sol = None
    maxh = 0
    while l<=r:

        print(f"{l}, {r}")
        m = l + ((r-l)>>1)
        oob, h = simulat(x, m)
        if oob:
            r = m-1
        else:
            maxh = max(maxh, h)
            curr_sol = maxh
            print(maxh)
            l = m + 1


    if curr_sol is None:
        return -1

    #oob, maxh = simulat(x, curr_sol)
    #assert not oob
    return maxh


mx = 0

for x in range(1, ax[1]+1):
    maxy = bsearch(x)
    mx = max(maxy, mx)

print(mx)
