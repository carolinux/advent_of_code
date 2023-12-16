
fn = 'day15.txt'
s = 0


def haash(seg):
    res = 0
    for ch in seg:
        val = ord(ch)
        res+=val
        res*=17
        res = res % 256

    return res

with open(fn, 'r') as f:
    segs = f.readline().strip().split(",")
    #print(segs)
    for seg in segs:
        s+=haash(seg)

print(s)
print(haash("ot"))
print(haash("pc"))
print(haash("cm"))
print(haash("rn"))
print(haash("qp"))
