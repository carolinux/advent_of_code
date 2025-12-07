


def cesar(ch, offset):
    ix = ord(ch) - ord('a')
    ix = (ix +offset) % 26
    ix = ord('a') + ix
    return chr(ix)


text ="kyzj fev nrj vrjp"
for i in range(26):
    text2 = []
    for ch in text:
        if ch == " ":
            text2.append(ch)
            continue
        ch2 = cesar(ch, i)
        text2.append(ch2)
    print(''.join(text2))
