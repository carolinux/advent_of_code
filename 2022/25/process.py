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


order = {

    '0':0,'1':1,'2':2,'=':3,'-':4

}


m = {

 ('0','0'): ('0','0'),
 ('0','1'): ('1','0'),
 ('0','2'): ('2','0'),
 ('0','='): ('=','0'),
 ('0','-'): ('-','0'),
 ('1','1'): ('2','0'),
 ('1','2'): ('=','1'),
 ('1','='): ('-','0'),
 ('1','-'): ('0','0'),
 ('2','2'): ('-','1'),
 ('2','='): ('0','0'),
 ('2','-'): ('1','0'),
 ('=','='): ('1','-1'),
 ('=','-'): ('2','-1'),
 ('-','-'): ('=','0'),

}

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


def nxt(d):
    o = order[d]
    for k,v in order.items():
        if v == o+1:
            return k

def prev(d):
    o = order[d]
    for k,v in order.items():
        if v == o-1:
            return k

def add_digits(d1, d2, curry):
    o1 = order[d1]
    o2 = order[d2]
    if o2< o1:
        tmp = d1
        d1 = d2
        d2 = tmp

    if d1=='-' and d2 =='-' and curry == '1':
        return ('-', '0')
    if curry == '0':
        res = m[(d1, d2)]
    elif curry == '-1':
        assert(not (d1=='0' and d2=='0'))
        if d1=='0':
            d2 = prev(d2)
        else:
            d1 = prev(d1)

        dd, cc = m[(d1, d2)]
        return dd,cc


    elif curry == '1':
        
        dd, cc = m[(d1, d2)]
        print('hhhhhhhh')
        return add_digits(dd, '1', cc)


    else:
        raise Exception("Should be unreachable")
    return res


def add(rnum1, rnum2):
    res = []
    print(rnum1)
    print(rnum2)


    rnum1.append('0')
    rnum1.append('0')

    curry = '0'

    for d1, d2 in itertools.zip_longest(rnum1, rnum2, fillvalue='0'):
        print(f" adding {d1}, {d2} with curry {curry}")

        digit, curry = add_digits(d1, d2, curry)
        print(f"res {digit}, curr={curry}")
        res.append(digit)


    return res




curr = add(rnums[0], rnums[1])
assert (to_int(curr) == to_int(rnums[0]) + to_int(rnums[1]))

for i in range(2, len(rnums)):
    prevv = to_int(curr)
    print(f"adding {rnums[i]}, {curr}")
    curr = add(rnums[i], curr)
    print (f"{to_int(curr)} == {to_int(rnums[i])} + {prevv}")
    assert (to_int(curr) == to_int(rnums[i]) + prevv)


print(to_int(curr))

curr.reverse()
print(''.join(curr))
