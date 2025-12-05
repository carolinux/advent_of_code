import sys
ans = 0
r = []
DIVS = {}
with open("input.txt", "r") as f:
    line = f.readline()
    ranges = line.split(",")
    for rang in ranges:
        #print(rang)
        rang = rang.strip()
        a, b = rang.split("-")
        r.append((int(a), int(b)))


def get_divs(digs):
    return DIVS[digs]


def find_divisors_generator(n):
    for i in range(1, int(n**0.5) + 1):  # Loop up to √n
        if n % i == 0:
            yield i
            if i != n // i  and i!=1:
                yield n // i      # Yield the paired divisor


for i in range(2, 20):
    divs = list(find_divisors_generator(i))
    DIVS[i] = divs


def process(a, b):
    s = 0
    print(f"{a}-{b}")
    for num in range(a, b+1):
        if num <10:
            continue
        sn = str(num)
        digs = len(sn)

        for div in get_divs(digs):
            leng = digs // div
            amount = digs // leng

            good = True

            for i in range(leng):
                slice = sn[i*amount: (i+1)*amount]
                #print(f"getting slice {i*amount} to ({(i+1)*amount}")
                if i >=1:
                    if slice != prevslice:
                        good = False
                        break
                prevslice = slice
            if good:
                #print(f"{num} is good for {div}, {slice}, {prevslice}")
                s+=num
                break



    return s

print(DIVS)
#sys.exit(0)
for a,b in r:
    ans+=process(a,b)

print(ans)
