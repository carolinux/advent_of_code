
fn = "input.txt"

hist = []
ans = 0
with open(fn, 'r') as f:
    for line in f.readlines():
        depth = int(line.strip())
        hist.append(depth)
        if len(hist) <4:
            continue
        sum1 = sum(hist[-4:-1])
        sum2 = sum(hist[-3:])
        if sum2 > sum1:
            ans+=1


print(ans)
