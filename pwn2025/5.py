import sys

def xor_bytes(a, b):
  return bytes([x ^ y for x, y in zip(a, b)])


m1 = "070d065214010206125307111d121a4b03160b450907080418451605001152111c0e4515121f1a52011b0c"


m2 = "150902151e060e100a1a0b042d1d1b193a12161c102d0c07340718173a130004171f0c1a1618"

m2 = m2 + "0" * (len(m2)-len(m1))

c1 = bytes.fromhex(m1)
c2 = bytes.fromhex(m2)

xored = xor_bytes(c1, c2)


crib = b"flag{"
result = xor_bytes(crib, xored[:len(crib)])
print(f"Crib '{crib.decode()}' at pos 0: {result}")

key1 = xor_bytes(b"flag{", c1)
print(key1)
key1 = xor_bytes(b"the q", c1)
print(key1) # this is "secre" so I try "secret" and "secretkey" as the keys!!

#Crib 'the ' at pos 31: b'acti'

pref = b'\x00' * 30 + b" "
key2 = xor_bytes(pref, c2)
print(len(key2))
print(key2)
#sys.exit(0)
key2 = key2[-4:]
print(key2)
#sys.exit(0)
for i in range(len(m1)):
    crib = b" an "
    result = xor_bytes(crib, xored[i:i+len(crib)])
    print(f"Crib '{crib.decode()}' at pos {i}: {result}")


key3 = b"secretkey"
print(len(key3))
k = 40 * key3

res1 = xor_bytes(c1, k)
print(res1)

res2 = xor_bytes(c2, k)
print(res2)
#print("------------")


