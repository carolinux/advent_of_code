
pos = 50
ans = 0
with open("input.txt", "r") as f:
    for line in f:
        line = line.strip()
        dir = line[0]
        num = int(line[1:])
        prevpos = pos
        if num > 99 :
            #print(num)
            ans += num//100
            num = num % 100

        if num == 0:
            continue

        if dir == "R":
            pos+=num
        else:
            pos-=num

        if (pos >= 100 or pos <= 0) and prevpos != 0:
            #print(f"incrementing after {line}")
            ans+=1

        pos%=100


print(ans)
