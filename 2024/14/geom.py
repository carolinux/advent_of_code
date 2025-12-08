
s = 0
prev = 1
for i in range(100):
    s+=prev
    prev+=2
    print(f"Value for i={i+1}={s}")



def top(i, j, rows, grid):
    for row in range(rows):
        st = j - row
        end = j + row + 1
        currr = i + row


        print(f"checking row {currr} {st}-{end-1}")

        for col in range(st, end, 1):
            if col<0 or currr<0 or col>=len(grid[0]) or currr>=len(grid):
                print("bad oob")
                return False, row+1
            if grid[currr][col] < 1:
                print("bad<1")
                return False, row+1
    return True, rows


grid = [[0, 1, 0],
        [1, 1, 1]]

grid = [[0, 0, 1, 0],
        [1, 1, 1, 1]]


print(top(0, 2, 2, grid))
