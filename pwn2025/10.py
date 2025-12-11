import sys
res = []
with open("10.txt", "r") as f:
    for i, line in enumerate(f):
        if i % 2 == 1:
            continue

        a,b = line.strip().split()
        ch = (int(b, 16).to_bytes(1, sys.byteorder))
        res.append(ch.decode("utf-8"))


print(''.join(res))

