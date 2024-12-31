

import sys


def mutat(num):
    num2 = num
    tmp=num<<6
    num2=(num2^tmp) % 16777216
    tmp=num2>>5
    num2=(num2^tmp) % 16777216
    tmp=num2<<11
    num2=(num2^tmp) % 16777216
    return num2



def process(num, iter):
    for i in range(iter):
        num2 = mutat(num)
        num = num2

    return num

def read_numbers_from_stdin():
    numbers = []
    for line in sys.stdin:
        try:
            number = int(line.strip())
            numbers.append(number)
        except ValueError:
            print(f"Skipping invalid input: {line.strip()}", file=sys.stderr)
    return numbers


nums = read_numbers_from_stdin()
ans = 0
for num in nums:
    ans+=process(num, 2000)

print(ans)
# 17262627539
