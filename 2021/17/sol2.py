

ax = (185, 221)
ay = (-122, -74)

#ax = (20, 30)
#ay =(-10, -5)



def simulat(vx, vy):
    x,y=(0,0)
    origvy = vy
    origvx = vx
    mx = 0
    step = 0
    while True:
        x+=vx
        y+=vy
        expy =  origvy * (step+1) - (((step+1)*step)>>1)
        assert y == expy, f"y={y}, expected ={expy} at step={step} with orgvy={origvy}"

        if step<origvx:
            expx =  origvx * (step+1) - (((step+1)*step)>>1)
        else:
            step2 = origvx
            expx =  origvx * (step2+1) - (((step2+1)*step2)>>1)

        assert x == expx, f"x={x}, expected ={expx} at step={step} with orgvx={origvx}"

        vy-=1
        if vx>0:
            vx-=1
        elif vx<0:
            vx+=1

        step+=1

        if x>ax[1] or y<ay[0]:
            return False

        if ax[0]<=x<=ax[1] and ay[0]<=y<=ay[1]:
            print(f"{origvx} {origvy} good")
            return True

    raise Exception("unreachable")





def search(x):
    r = 1000 # set randomly
    ans = 0

    for y in range(-r, r):
        #print(f"{x}, {y}")
        ans+=simulat(x, y)
    return ans


ans  = 0

for x in range(1, ax[1]+1):
    print(x)
    ans+=search(x)


print(ans)
