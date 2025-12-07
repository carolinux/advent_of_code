


def cesar(ch, offset):
    ix = ord(ch) - ord('a')
    ix = (ix + offset) % 26
    ix = ord('a') + ix
    return chr(ix)

def vigenere(ch, ix):
    ix = ix % len(VKEY)
    chk = VKEY[ix]
    #print(chk)
    offset = ord(chk) - ord('A')
    #print(offset)
    return cesar(ch, -offset)


VKEY = 'RUDOLF'

text ="wfdu{emv mhqcjkm rt emv hrfem gios}"
ix = 0

text2 = []
for ch in text:
    if ch == " " or ch == "{" or ch == "}":
        if ch == " ":
            ch = "_"
        text2.append(ch)
        continue
    ch2 = vigenere(ch, ix)
    text2.append(ch2)
    ix+=1
print(''.join(text2))
