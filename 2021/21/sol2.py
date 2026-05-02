
p1 = 10
p2 = 2

#p1 = 4
#p2 = 8


sc1 = 0
sc2 = 0
i = 0


def dicey():
    dice = 1
    while True:
        print(f"used dice={dice}")
        yield dice

        dice+=1
        if dice>100:
            dice=1

dice = dicey()

while True:


    throw = sum([next(dice) for _ in range(3)])
    if i%2 == 0:
        p1+=throw
        if p1 > 10:
            p1 = (p1 % 10)
            if p1  == 0:
                p1 = 10
        sc1+=p1
        if sc1 >= 1000:
            print((i+1)*3*sc2)
            break

    else:
        p2+=throw
        if p2>10:
            p2 = (p2 % 10)
            if p2 == 0:
                p2 = 10
        sc2+=p2
        if sc2 >= 1000:
            print((i+1)*3*sc1)
            break


    print(f"p1: {p1} sc1={sc1} | p2: p2={p2} {sc2}")


    i+=1
    #if i >10:
    #    break

print(f"p1: {p1} sc1={sc1} | p2: p2={p2} {sc2}")
print(f"after {(i+1)*3} rools")
