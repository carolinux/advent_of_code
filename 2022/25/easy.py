import itertools
import sys

fn = sys.argv[1]

rnums = []
with open(fn, 'r') as f:
    for line in f:
        num = list(line.strip())
        num.reverse()
        num.append('0')
        rnums.append(num)



def to_int(curr):
    res = 0
    base = 5
    poow = 1
    for d in curr:
        if d == '=':
            d = -2
        elif d == '-':
            d = -1
        else:
            d = int(d)
        res += d * poow
        poow *=base
    return res





curr = to_int(rnums[0]) + to_int(rnums[1])

for i in range(2, len(rnums)):
    curr += to_int(rnums[i])

def to_weird(num):

    # are those updated correctly in the loop ?
    base = 5
    res = []
    curry = 0
    while num:
        print(f"num mod base -> {num}")
        digit = num % (base)
        num = num // base
        digit+=curry

        assert(digit>=0)
        if digit<=2:
            res.append(str(digit))
            curry = 0
            continue

        if digit == 3:
            res.append("=")
            curry = 1
            continue

        if digit == 4:
            res.append('-')
            curry = 1
            continue

        if digit == 5:
            res.append('0')
            curry = 1 
            continue
        raise Exception()



    if curry == 1:
        res.append('1')


    res.reverse()
    res1= ''.join(res)
    print(res1)
    return res1






print(curr)
res1 = to_weird(curr)
print(f"weirdness {res1}")
print(f"matching int {to_int(reversed(res1))}")


#assert (to_weird(5) == '10')
#assert (to_weird(3) == '1=')
#assert (to_weird(7) == '12')
#assert (to_weird(201) == '2=01')
