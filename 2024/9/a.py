s = input().strip()


# free spaces = odd indexes from 1
# files = even indexes from n or n-1, whatever is even

blocks = []
id = 0
for i,ch in enumerate(s):
    dig = int(ch)
    if dig == 0:
        continue
    if i % 2 == 0:
        for _ in range(dig):
            blocks.append(id)
        id+=1
    else:
        for _ in range(dig):
            blocks.append(-1)

l = 0
r = len(blocks) - 1

while l<r:
    if blocks[l] !=-1:
        l+=1
        continue
    if blocks[r] == -1:
        r-=1
        continue

    blocks[l], blocks[r] = blocks[r], blocks[l]
    r-=1
    l+=1
ans  = 0
for i, b in enumerate(blocks):
    if b == -1:
        continue

    ans+=i*b
print(ans)

