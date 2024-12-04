import re
s = input().strip()
s+=input().strip()
s+=input().strip()
s+=input().strip()
s+=input().strip()
s+=input().strip()



i = 0

def parse_num(s, i):
    num = 0
    digs = 0
    while i < len(s):
        dig = s[i]
        if dig not in ('0123456789'):
            if not digs:
                return None, -1
            else:
                return num, i

        digs+=1
        num = num * 10 + int(dig)
        i+=1


def try_mul(s, i):
    if s[i: i+ len("mul(")] != "mul(":
        return i+1, 0
    num, new_i = parse_num(s, i+len("mul("))
    if num is None:
        return i+1, 0

    if new_i>=len(s) or s[new_i] !=',':
        return i+1, 0
    num2, new_i = parse_num(s, new_i+1)
    if num2 is None:
        return i+1, 0
    if new_i>=len(s) or s[new_i]!=")":
        return i+1, 0
    print(f"{num}x{num2} found in {s[i:new_i+1]}")
    return new_i+1, num * num2

def try_on(s, i):
    return s[i:i+len("do()")] == "do()"

def try_off(s, i):
    return s[i:i+len("don't()")] == "don't()"

ans = 0
on = True
while i < len(s):
    if on:
        if s[i] == 'm':
            new_i, incr = try_mul(s, i)
            ans+=incr
        else:
            if try_off(s, i):
                on = False
            new_i = i+1

    else:
        if try_on(s, i):
            on = True
        new_i = i+1

    i = new_i

print(ans)


