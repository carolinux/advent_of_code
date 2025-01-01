# locks: top row filled
# keys: bottom row filled

# 5x5
# with two extra rows
import sys
def parse_matrices(input_string):
    raw_matrices = input_string.strip().split("\n\n")
    locks = []
    keys = []
    for raw_matrix in raw_matrices:
        matrix = [list(line) for line in raw_matrix.splitlines()]
        heights = []
        if len(matrix) == 7 and all(len(row) == 5 for row in matrix):
            if all(x == '.' for x in matrix[0]):
                for col in range(5):

                    for row in range(0, 7):
                        if matrix[row][col] == '#':
                            heights.append(6-row)
                            break
                keys.append(heights)
            else:
                for col in range(5):
                    #print(f"col:{col}")
                    for row in range(6, -1, -1):
                        if matrix[row][col] == '#':
                            heights.append(row)
                            break

                locks.append(heights)
        else:
            raise ValueError("Each matrix must be 7 rows by 5 columns.")

    return locks, keys



locks, keys = parse_matrices(sys.stdin.read())

#print(locks)
#print(keys)
ans = 0
for lock in locks:
    for key in keys:
        good = True
        for l, k in zip(lock, key):
            if l + k >=6:
                good = False
                break
        if good:
            ans+=1


print(ans)
