"""
description:

Given
n = 100160063

e = 65537

c = 43689330

Task
Factor n into p and q, compute d = modular inverse of e mod (p-1)(q-1), decrypt c to a plaintext number, then submit flag{that_number}.

Example
If n=15, e=3, c=8 → p=3, q=5, d=3, plaintext=2 → flag{2}

from: https://en.wikipedia.org/wiki/RSA_cryptosystem

Alice can recover m from c by using her private key exponent d by computing

c^ d ≡ ( m ^e ) d ≡ m ( mod n ) . {\displaystyle c^{d}\equiv (m^{e})^{d}\equiv m{\pmod {n}}.}


"""
import math

n = 100160063

e = 65537

c = 43689330

def divs(num):
    sq = int(math.sqrt(n))
    for i in range(2, sq+1):
        if num%i == 0:
            p = i
            q = num // p
            return p, q


p, q = divs(n)
print(p, q)
modulo = (p-1)*(q-1)
d = pow(e, -1, modulo)
cleartext = pow(c, d, n)
print(cleartext)


