
s = 0

def process(a):
    lasts = [a[-1]]
    while True:
        b = []
        for i in range(1, len(a)):
            b.append(a[i]-a[i-1])


        if all([x == 0 for x in b]):

            break

        lasts.append(b[-1])

        a = b

    curr = 0
    for j in range(len(lasts)-1, -1, -1):
        curr = curr + lasts[j]


    return curr


with open("aoc9.txt", 'r') as f:


    for line in f.readlines():
        a = [int(x) for x in line.split()]
        s+=process(a)





print(s)


