import sys
from collections import Counter
fn = "input.txt"
#fn = "small.txt"

ans = 0

SCORE = {
    ')': 3, ']': 57, '}':1197, '>': 25137,
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
                return SCORE[ch]
            opens.pop()

    return 0




with open(fn, "r") as f:
    for line in f.readlines():
        line = line.strip()
        ans+=solve(line)

print(ans)
