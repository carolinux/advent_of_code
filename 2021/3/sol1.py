fn = "input.txt"


def arr_to_bin(a):
    num = 0
    for i in range(len(a)):
        num<<=1
        num+=a[i]
    return num



ans = 0
cnts1 = [0] * 12
cnt = 0
with open(fn, 'r') as f:
    for line in f.readlines():
        num = line.strip()
        print(num)
        for i in range(len(num)):
            if num[i] == "1":
                cnts1[i]+=1
        cnt+=1


gamma = [0] * 12
epsilon = [0] * 12

for i in range(12):
    zeroes = cnt - cnts1[i]
    ones = cnts1[i]
    gamma[i] = 1 if ones>zeroes else 0
    epsilon[i] = 1 - gamma[i]


ans = arr_to_bin(gamma) * arr_to_bin(epsilon)
print(ans)





