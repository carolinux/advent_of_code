
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
    nums = [num]
    for i in range(iter):
        num2 = mutat(num)
        num = num2
        nums.append(num)

    return nums

def read_numbers_from_stdin():
    numbers = []
    for line in sys.stdin:
        try:
            number = int(line.strip())
            numbers.append(number)
            assert number > 0
        except ValueError:
            raise Exception(f"Skipping invalid input: {line.strip()}")
    return numbers

def diffy(nums):
    diffs = []
    for i in range(1, len(nums)):
        diffs.append((nums[i]%10) - (nums[i-1]%10))
    #print(f"Diffs={diffs} for nums={nums}")
    mseq = {}
    for i in range(3, len(diffs)):
        assert i-3 >= 0
        seq4 = (diffs[i-3], diffs[i-2], diffs[i-1], diffs[i])
        mseq[seq4] = max(mseq.get(seq4, 0), nums[i+1]%10)

    return mseq



nums = read_numbers_from_stdin()

changes = set()
diffs = []
for num in nums:
    curr = process(num, 2000)
    #assert(len(curr) == 2001)
    diff = diffy(curr)
    diffs.append(diff)
    for seq4 in diff:
        changes.add(seq4)

ans = 0

print(len(nums))
#print(nums)

for j, cand in enumerate(changes):

    #print(f"looking at sequence {cand} {j} out of {len(changes)}")
    candprice = 0
    for i, diff in enumerate(diffs):
        candprice+=diff.get(cand, 0)

    if candprice > ans:
        ans = candprice
        print(f"best {cand}")


print(ans)


