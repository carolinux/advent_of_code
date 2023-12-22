
def get_neighbours(pt, mat, visited=None, badvals=None):
    rows = len(mat)
    cols = len(mat[0])
    x,y = pt
    ans = []
    for dx, dy in ((0,1),(0,-1),(1,0),(-1,0)):
        cx = x + dx
        cy = y + dy
        if cx<0 or cy<0 or cx>=rows or cy>=cols:
            continue
        cpt = (cx, cy)
        if visited is not None and cpt in visited:
            continue
        if badvals is not None and mat[cx][cy] in badvals:
            continue
        ans.append(cpt)
    return ans


def read_str_mat(fn):
    mat = []
    with open(fn, 'r') as f:
        for line in f.readlines():
            row = list(line.strip())
            mat.append(row)

    return mat

def print_mat(mat):
    for row in mat:
        print("".join(row))
