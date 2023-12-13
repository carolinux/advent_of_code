
def process(mat):
    rows = len(mat)
    cols = len(mat[0])
    # I will find the highest reflected row
    mr = find_refl(mat)

    # turn into cols x rows
    mat2 = []

    for j in range(cols):
        col = []
        for i in range(rows):
            col.append(mat[i][j])
        mat2.append(col)

    mc = find_refl(mat2)
    print(f"Found {mr}, {mc}")
    return mr, mc


def find_refl(mat):
    mr = 0
    rows = len(mat)
    for i in range(rows - 1):
        if mat[i] == mat[i + 1]:
            valid = True
            for j in range(1, rows):
                if i - j < 0 or i + j + 1 >= rows:
                    break
                if mat[i - j] != mat[i + j + 1]:
                    valid = False
            if valid:
                mr = max(mr, i + 1)
    return mr


s = 0
mat = []
# I added a blank line at the end of my input
with open("day13.txt", 'r') as f:

    for i,line in enumerate(f.readlines()):

        #print(f"line={line}, {line.strip() == ''} ")
        if line.strip() == '':
            r,c = process(mat)
            incr = 100*r + c
            s+=incr
            mat = []
        else:
            row = list(line.strip())
            mat.append(row)

print(s)





