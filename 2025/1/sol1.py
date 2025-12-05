
pos = 50
ans = 0
with open("input.txt", "r") as f:
    for line in f:
        line = line.strip()
        dir = line[0]
        num = int(line[1:])

        if dir == "R":
            pos+=num
        else:
            pos-=num

        pos%=100

        if pos == 0:
            ans+=1
print(ans)
