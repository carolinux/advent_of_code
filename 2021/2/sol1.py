fn = "input.txt"


diffs = {"forward": (0, 1), "down": (1, 0), "up": (-1, 0)}
def tadd(tupl1, tupl2):
    return tupl1[0]+tupl2[0], tupl1[1]+tupl2[1]

def tmult(tupl, mul):
    return tupl[0]*mul, tupl[1] * mul


ans = 0
pos = (0, 0)
with open(fn, 'r') as f:
    for line in f.readlines():
        parts = line.strip().split()
        diff = tmult(diffs[parts[0]], int(parts[1]))
        pos = tadd(pos, diff)

print(pos[0]*pos[1])


