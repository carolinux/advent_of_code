"""
Santa and the Grinch are doing Diffie-Hellman on a small prime for testing.
You intercepted everything.

Given
p = 23

g = 5

A = 8

B = 19

Task
Compute the shared secret s = g^(ab) mod p = A^b mod p = B^a mod p.
Submit flag{sha256(hex(s))[:40]} (lowercase).

Example
If p=23, g=5, A=8, B=19 → a=6, b=15, s=2 → flag{d4735e3a265e16eee03f59718b9b5d03019c07d8}


wikipedia

Only a and b are kept secret. All the other values – p, g, ga mod p, and gb mod p – are sent in the clear.
 The strength of the scheme comes from the fact that gab mod p = gba mod p take extremely long times to compute
 by any known algorithm just from the knowledge of p, g, ga mod p, and gb mod p. Such a function that is easy to compute
  but hard to invert is called a one-way function. Once Alice and Bob compute the shared secret
   they can use it as an encryption key, known only to them, for sending messages across
    the same open communications channel.


"""

p = 23

g = 5

A = 8

B = 19

aas = []
bs = []

for a in range(1, 1000):
    # A = g**(a) mod p
    if pow(g, a, p) == A:
        print(f"possible ={a}")
        aas.append(a)

print("-----------------------")
for b in range(1, 1000):
    # B = g**(b) mod p
    if pow(g, b, p) == B:
        print(f"possible ={b}")
        bs.append(b)



secrets = set()
for a in aas:
    for b in bs:
        sg = pow(g, a*b, p)
        vala = pow(A, b, p)
        valb = pow(B, a, p)
        if vala == valb == sg:
            print(f"found: {a}, {b}, {sg}")
            secrets.add(sg)

print(secrets) # just {2}


import hashlib
hex_s = "2"
hash_result = hashlib.sha256(hex_s.encode()).hexdigest()[:40]
print(hash_result)

