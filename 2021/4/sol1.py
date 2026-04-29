import sys
fn = "input.txt"



ans = 0
mats = []
cnt = 0
# parsety parse
with open(fn, 'r') as f:
    for line in f.readlines():
        if cnt == 0:
            nums = list(line.strip().split(","))
            #print(nums)
            xnums = [int(x) for x in nums]
            cnt+=1
            continue
        if line.strip() == "":
            cnt+=1
            continue
        if (cnt +4 ) % 6 == 0:
            mat = []
        nums = list(line.strip().split(" "))
        nums =[int(x) for x in nums if x !=""]
        assert len(nums) == 5
        mat.append(nums)
        if (cnt+4) % 6 == 4:
            mats.append(mat)
            assert len(mat) == 5, f"{len(mat)}\n{mat}"
        cnt+=1

def process(mat, targ):
    s = 0
    for i in range(5):
        for j in range(5):
            if mat[i][j] == targ:
                mat[i][j] = -1
            elif mat[i][j] !=-1:
                s+= mat[i][j]

    for i in range(5):
        if all(mat[i][x] == -1 for x in range(5)):
            return True, s
        if all(mat[x][i] == -1 for x in range(5)):
            return True, s

    #print(f"{mat[0]}, targ={targ}")

    return False, s


wins = set()

for num in xnums:
    for mi, mat in enumerate(mats):
        if mi in wins:
            continue
        won, s = process(mat, num)
        if won:
            # first output is answer to part1, last output is answer to part2
            wins.add(mi)
            print(s*num)
            #sys.exit(0)




