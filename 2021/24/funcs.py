def block1(z, w):
    x = 0
    x += z
    x %= 26
    z //= 1
    x += 11
    x = 1 if x == w else 0
    x = 1 if x == 0 else 0
    y = 0
    y += 25
    y *= x
    y += 1
    z *= y
    y = 0
    y += w
    y += 1
    y *= x
    z += y
    return z


def block2(z, w):
    x = 0
    x += z
    x %= 26
    z //= 1
    x += 11
    x = 1 if x == w else 0
    x = 1 if x == 0 else 0
    y = 0
    y += 25
    y *= x
    y += 1
    z *= y
    y = 0
    y += w
    y += 11
    y *= x
    z += y
    return z


def block3(z, w):
    x = 0
    x += z
    x %= 26
    z //= 1
    x += 14
    x = 1 if x == w else 0
    x = 1 if x == 0 else 0
    y = 0
    y += 25
    y *= x
    y += 1
    z *= y
    y = 0
    y += w
    y += 1
    y *= x
    z += y
    return z


def block4(z, w):
    x = 0
    x += z
    x %= 26
    z //= 1
    x += 11
    x = 1 if x == w else 0
    x = 1 if x == 0 else 0
    y = 0
    y += 25
    y *= x
    y += 1
    z *= y
    y = 0
    y += w
    y += 11
    y *= x
    z += y
    return z


def block5(z, w):
    x = 0
    x += z
    x %= 26
    z //= 26
    x += -8
    x = 1 if x == w else 0
    x = 1 if x == 0 else 0
    y = 0
    y += 25
    y *= x
    y += 1
    z *= y
    y = 0
    y += w
    y += 2
    y *= x
    z += y
    return z


def block6(z, w):
    x = 0
    x += z
    x %= 26
    z //= 26
    x += -5
    x = 1 if x == w else 0
    x = 1 if x == 0 else 0
    y = 0
    y += 25
    y *= x
    y += 1
    z *= y
    y = 0
    y += w
    y += 9
    y *= x
    z += y
    return z


def block7(z, w):
    x = 0
    x += z
    x %= 26
    z //= 1
    x += 11
    x = 1 if x == w else 0
    x = 1 if x == 0 else 0
    y = 0
    y += 25
    y *= x
    y += 1
    z *= y
    y = 0
    y += w
    y += 7
    y *= x
    z += y
    return z


def block8(z, w):
    x = 0
    x += z
    x %= 26
    z //= 26
    x += -13
    x = 1 if x == w else 0
    x = 1 if x == 0 else 0
    y = 0
    y += 25
    y *= x
    y += 1
    z *= y
    y = 0
    y += w
    y += 11
    y *= x
    z += y
    return z


def block9(z, w):
    x = 0
    x += z
    x %= 26
    z //= 1
    x += 12
    x = 1 if x == w else 0
    x = 1 if x == 0 else 0
    y = 0
    y += 25
    y *= x
    y += 1
    z *= y
    y = 0
    y += w
    y += 6
    y *= x
    z += y
    return z


def block10(z, w):
    x = 0
    x += z
    x %= 26
    z //= 26
    x += -1
    x = 1 if x == w else 0
    x = 1 if x == 0 else 0
    y = 0
    y += 25
    y *= x
    y += 1
    z *= y
    y = 0
    y += w
    y += 15
    y *= x
    z += y
    return z


def block11(z, w):
    x = 0
    x += z
    x %= 26
    z //= 1
    x += 14
    x = 1 if x == w else 0
    x = 1 if x == 0 else 0
    y = 0
    y += 25
    y *= x
    y += 1
    z *= y
    y = 0
    y += w
    y += 7
    y *= x
    z += y
    return z


def block12(z, w):
    x = 0
    x += z
    x %= 26
    z //= 26
    x += -5
    x = 1 if x == w else 0
    x = 1 if x == 0 else 0
    y = 0
    y += 25
    y *= x
    y += 1
    z *= y
    y = 0
    y += w
    y += 1
    y *= x
    z += y
    return z


def block13(z, w):
    x = 0
    x += z
    x %= 26
    z //= 26
    x += -4
    x = 1 if x == w else 0
    x = 1 if x == 0 else 0
    y = 0
    y += 25
    y *= x
    y += 1
    z *= y
    y = 0
    y += w
    y += 8
    y *= x
    z += y
    return z


def block14(z, w):
    x = 0
    x += z
    x %= 26
    z //= 26
    x += -8
    x = 1 if x == w else 0
    x = 1 if x == 0 else 0
    y = 0
    y += 25
    y *= x
    y += 1
    z *= y
    y = 0
    y += w
    y += 6
    y *= x
    #print(f"z={z} y={y} they should be negatable")
    z += y

    return z


BLOCKS = [
    block1, block2, block3, block4, block5, block6, block7,
    block8, block9, block10, block11, block12, block13, block14,
]
