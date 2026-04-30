import sys
from collections import Counter
fn = "input.txt"
#fn = "small.txt"

ans = 0

SCORE = {
    ')': 3, ']': 57, '}':1197, '>': 25137,
    # part2
    '(': 1, '[':2, '{':3, '<':4,
}




REV ={
    ')':'(', '}':'{', '>':'<', ']':'[',

}

def solve(line):
    opens = []

    for ch in line:
        if ch in '([<{':
            opens.append(ch)
        else:
            rch = REV[ch]
            if len(opens) == 0 or opens[-1] !=rch:
                return 0
            opens.pop()

    res = 0
    while len(opens) > 0:
        res*=5
        ch = opens.pop()
        res+=SCORE[ch]
    return res



scores = []
with open(fn, "r") as f:
    for line in f.readlines():
        line = line.strip()
        sc = solve(line)
        if sc >0:
            scores.append(sc)


scores.sort()
print(scores[len(scores)>>1])
