nums = []
m = 0
with open('mixed_file.txt', 'r') as f:
    for line in f:
        a = int(line.strip())
        nums.append(a)

        m = max(a, m)


print(len(nums))
print(len(set(nums)))
print(m)
print(min(nums))
