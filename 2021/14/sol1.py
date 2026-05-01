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

"""
for ch1 in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    for ch2 in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        s = ch1+ch2
        if s not in rules:
            continue
"""
s = curr
print(s)
iterats = 10
for it in range(iterats):
    #print(it)
    parts = []
    for i in range(len(s)-1):
        ch1 = s[i]
        ch3 = s[i+1]
        ch2 = rules[ch1+ch3]
        parts.append(ch1+ch2)
        if i == len(s) -2 :
            parts.append(ch3)

    s = ''.join(parts)
    print(f"it {it}")
    print(Counter(s))
    #if it < 5:
    #    print(s)

cnt = Counter(s)
vals = list(cnt.values())
vals.sort()
print(vals[-1]-vals[0])
#print(cnt)



