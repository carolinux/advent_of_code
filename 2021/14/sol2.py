import sys
from collections import Counter, deque, defaultdict
fn = "input.txt"
#fn = "small.txt"

ans = 0


g = defaultdict(list)
rules = {}

with open(fn, "r") as f:
    for line in f.readlines():
        line = line.strip()
        if "-" not in line and line !="":
            curr = line
            continue
        if line == "":
            continue
        parts = line.split(" -> ")
        a = parts[0]
        b = parts[1]
        rules[a]=b


s = curr
print(s)

cnt = Counter()

for i in range(len(s)-1):
    if i == 0:
        ch0 = "."
    else:
        ch0 = s[i-1]
    if i == len(s) - 2:
        ch3 = "."
    else:
        ch3 = s[i+2]
    ch1 = s[i]
    ch2 = s[i+1]
    elem = ch0+ch1+ch2+ch3
    cnt[elem]+=1


iterats = 40
for it in range(iterats):
    cnt2 = Counter()
    cnt3 = Counter()
    for elem, count in cnt.items():
        v = elem[1:3]
        newch = rules[v]
        ch0 = elem[0]
        ch1 = elem[1]
        ch2 = elem[2]
        ch3 = elem[3]

        new1 = ch0+ch1+newch+ch2
        new2 = ch1+newch+ch2+ch3
        cnt2[new1]+=count
        cnt2[new2]+=count
        #print(f"old= {ch1}{ch2}, new ={ch1} {newch} {ch2}")
        cnt3[ch1]+=count
        cnt3[newch]+=count
        if ch3 == '.':
            cnt3[ch2]+=count


    print(f"iterat: {it}")
    print(cnt3)
    cnt = cnt2
    #break

#cnt3 = Counter()
#for val,count in cnt.items():
#    ch1 = val[1]
#    ch2 =val[2]
#    cnt3[ch1]+=count
#    cnt3[ch2]+=count

print(cnt3)
vals = list(cnt3.values())
print(vals)
vals.sort()
print(vals[-1]-vals[0])



