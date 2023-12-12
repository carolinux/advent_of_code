import functools as ft


@ft.lru_cache(maxsize=None)
def ways(gi, cursor, ch, id):

    if gi == len(groups) and ch =='#' and cursor != len(pattern):
        return 0

    if cursor == len(pattern) and ch == '#':
        if gi == len(groups):
            return 1
        else:
            return 0

    ans = 0
    if ch == '.':
        if gi == 0 or gi == len(groups):
            ans += ways(gi, cursor, '#', id)
        left = len(pattern) - cursor

        for lng in range(1, left+1):
            if pattern[cursor + lng - 1] == '#':
                break
            ans += ways(gi, cursor + lng, '#', id)
    else:
        valid = True
        lng = groups[gi]
        for j in range(cursor, cursor + lng):
            if j >= len(pattern) or pattern[j] == '.':
                valid = False
                break

        if valid:
            ans += ways(gi+1, cursor + lng, '.', id)
    return ans

s = 0
with open("day12.txt", 'r') as f:

    for i,line in enumerate(f.readlines()):
        pattern, groups = line.strip().split(' ')
        pattern = pattern + '?' + pattern + '?' + pattern + '?' + pattern + '?' + pattern
        groups = list(map(int, groups.split(',')))
        groups = 5 * groups
        w = ways(0, 0, '.', i)
        s+=w

print(s)
