import functools as ft
import math

def parse_input(input_text):
    registers = {}
    program = []

    for line in input_text.strip().split("\n"):
        if line.startswith("Register"):
            parts = line.split(":")
            register_name = parts[0].strip().split(" ")[1]
            value = int(parts[1].strip())
            registers[register_name] = value
        elif line.startswith("Program"):
            parts = line.split(":")
            program = [int(x.strip()) for x in parts[1].split(",")]
    return registers, program


import sys

input_text = sys.stdin.read()
regs, ops = parse_input(input_text)

print(regs)
#print(ops)

def combine(bs):
    num  = 0
    shift = 0
    for i in range(len(bs)-1, -1, -1):
        num = num + (bs[i]<<shift)
        shift+=3
    return num



res = []
@ft.lru_cache(maxsize=None)
def process(b1,b2,b3,b4, i, j):
    if i == len(ops):
        return 0
    b = b4^6
    c = combine([b1,b2,b3,b4]) >> b
    cand = (b^c^4)&7

    if cand != ops[i]:
        return -1
    if False:
        pass
    else:
        for b0 in range(8):
            prev = process(b0, b1, b2, b3, i+1, j+1)
            if prev !=-1:
                return (prev<<3) | b0

    return -1


ans = math.inf

for i in range(8):
    for j in range(8):
        for k in range(8):
            for l in range(8):
                cand = process(i, j, k, l, 0, 4)
                if cand !=-1:
                    cand = (cand<<3) | i
                    cand = (cand<<3) | j
                    cand = (cand<<3) | k
                    cand = (cand<<3) | l
                    ans = min(ans, cand)


print(ans)
assert ans >(2**46) and ans < (2**47)





