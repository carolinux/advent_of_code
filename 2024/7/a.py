import sys
T = 850
#T = 9

ans = 0


def concat(num1, num2):
    shifts = len(str(num2))
    return (num1 * 10**shifts) + num2


#print(concat(12, 34))

#sys.exit(0)


for i in range(T):
    line = input().strip()
    parts = line.split(":")
    res = int(parts[0])
    vals1 = parts[1].split(" ")
    vals = []
    for v in vals1:
        if v == '':
            continue
        vals.append(int(v))


    def verif(ix, curr, targ):
        if curr > targ:
            return False # can do this since no negative numbers or 0s in my input
        if ix == len(vals)-1:
            if curr != targ:
                return False
            return True

        cand1 = verif(ix+1, curr + vals[ix+1], targ)
        cand2 = verif(ix+1, curr * vals[ix+1], targ)
        cand3 = verif(ix+1, concat(curr, vals[ix+1]), targ) # only relevant for part II
        return cand1 or cand2 or cand3

    if verif(0, vals[0], res):
        ans+=res

print(ans)
