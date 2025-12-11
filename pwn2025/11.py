import sys
ct = '2803131313230a00036d5457563c160200013e0833065d545748' # split by two
key = 'NorthPole2025'  # convert each char to 8bit hex
keylen = len(key)

keybytes = []
for ch in key:
    hex = ch.encode('utf-8').hex()
    keybytes.append(hex)

print(keybytes)
#assert len(keybytes) == keylen
#sys.exit(0)
#print(len(ct))
res = []
for i in range(0, len(ct), 2):
    bytestr = f"{ct[i]}{ct[i+1]}"
    #print(bytestr)
    byte1 = int(bytestr, 16).to_bytes(1, sys.byteorder)
    #print(byte1)
    j = (i>>1) % keylen
    byte2str = keybytes[j]
    #print(f"aaa{byte2str}")
    byte2 = int(byte2str, 16).to_bytes(1, sys.byteorder)
    xorr = byte2[0]^byte1[0]

    res.append(xorr.to_bytes(1, sys.byteorder).decode("utf-8"))

print(''.join(res))
