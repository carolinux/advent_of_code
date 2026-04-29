import copy

fn = "input.txt"
LEN = 12

def arr_to_bin(a):
    num = 0
    for i in range(len(a)):
        num<<=1
        num+=a[i]
    print(num)
    return num

ans = 0
nums = []
cnt = 0
with open(fn, 'r') as f:
    for line in f.readlines():
        num = list(line.strip())
        cnt+=1
        nums.append([int(x) for x in num])

#print(nums)

def get_ones(nums, ix):
    ones=0;zeroes=0
    for num in nums:
        if num[ix] == 1:
            ones+=1
        else:
            zeroes+=1
    return ones, zeroes

curra = copy.copy(nums)
currb = copy.copy(nums)
for i in range(LEN):
    oa,za = get_ones(curra, i)
    ob,zb = get_ones(currb, i)
    bita = 1 if oa>=za else 0
    #print(f"bit for a={bita}, {oa} out of {oa+za}")
    bitb = 1 if ob<zb else 0
    curra2 = []
    currb2 = []
    if len(curra) > 1:
        for num in curra:
            if num[i] == bita:
                curra2.append(num)

        curra = curra2

    if len(currb) > 1:
        for num in currb:
            if num[i] == bitb:
                currb2.append(num)

        currb = currb2



ans = arr_to_bin(curra[0]) * arr_to_bin(currb[0])
print(ans)





