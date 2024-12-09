import sys
s = input().strip()


# free spaces = odd indexes from 1
# files = even indexes from n or n-1, whatever is even

blocks = []
empties = []
id = 0
s2 = []
for i,ch in enumerate(s):
    dig = int(ch)
    if dig == 0:
        continue
    if i % 2 == 0:
        blocks.append((dig, id, len(s2)))
        for _ in range(dig):
            s2.append(id)
        id+=1
    else:
        empties.append((dig, len(s2)))
        for _ in range(dig):
            s2.append('.')


for i in range(len(blocks)-1, -1, -1):
    bsize, bid, bix = blocks[i]
    last = None
    e = len(empties)
    for ii in range(e):
        esize, eix = empties[ii]
        if esize < bsize or eix>=bix:
            continue
        for j in range(bsize):
            s2[eix+j] = bid
            s2[bix+j] = '.'

        if esize-bsize > 0:
            new = (esize-bsize, eix+j+1)
            empties = empties[:ii] + [new] + empties[ii+1:]
        else:
            #print(empties)
            empties = empties[:ii] + empties[ii+1:]

        break

ans = 0

for i in range(len(s2)):
    if s2[i] == '.':
        continue
    ans+=i*s2[i]

print(ans)





