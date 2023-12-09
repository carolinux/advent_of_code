
Ar = 1590
Br = 160

As = 9186
Bs = 905

Ah = 2524
Bh = 272



tril = 10**12


ix = (tril+Br)//(Ar+Br)


si = ix * As + (ix-1) * Bs

print(f"ix={ix}")
print(f"We want to start at {si+1}")

height = ix * Ah + (ix-1)* Bh

print(f"We want to add {height} to the small result")

rocks = ix * Ar + (ix-1) * Br

rocks+=1

print(f"Remainign rocks: {tril -rocks}")

print(height + 1454)
