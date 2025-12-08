
def parse_input(input_text):
    registers = {}
    program = []

    for line in input_text.strip().split("\n"):
        if line.startswith("Register"):
            parts = line.split(":")
            register_name = parts[0].strip().split(" ")[1]
            value = int(parts[1].strip())
            registers[register_name] = value
        elif line.startswith("Program"):
            parts = line.split(":")
            program = [int(x.strip()) for x in parts[1].split(",")]
    return registers, program


def parse_2nd_operand(ix):
    if ix == 7:
        raise Exception("something went wrong")
    if ix <=3:
        return ix
    if ix ==4:
        return regs['A']
    if ix == 5:
        return regs['B']
    if ix == 6:
        return regs['C']

import sys

input_text = sys.stdin.read()
regs, ops = parse_input(input_text)

print(regs)
#print(ops)

def process(ai, regs, ops, verbose=True):
    out = []
    i = 0
    regs['A'] = ai
    origai = regs['A']
    aas = [bin(origai)]
    while i<len(ops):
        op = ops[i]
        operand = ops[i+1]
        if op == 0:
            val = regs['A']
            pow = parse_2nd_operand(operand)
            if verbose:
                print(f"a= dividing {val} by {2**pow}= {val // (2**pow)}")
            regs['A'] = val // (2**pow)
        elif op == 1:
            val = regs['B']
            val2 = operand
            if verbose:
                print(f"b= xor {val} with lit{val2} = {val ^ val2} {regs}")
            regs['B'] = val ^ val2
        elif op == 2:
            val = parse_2nd_operand(operand) % 8
            if verbose:
                print(f"b= {val} (kept lowest 3 bits of {bin(regs['A'])}/{regs['A']}")
            regs['B'] = val
        elif op == 3:
            #print(f"before jump, regs={regs},  (origai={origai})")
            aas.append(bin(regs['A']))
            if regs['A'] == 0:
                i+=2
                continue
            else:
                i = operand
                continue
        elif op == 4:
            if verbose:
                print(f"b= {regs['B']} xor {regs['C']}= {regs['B'] ^ regs['C']}")
            regs['B'] = regs['B'] ^ regs['C']
        elif op == 5:

            val = parse_2nd_operand(operand) % 8
            if verbose:
                print(f"printing {val} (kept lowest 3 bits of {bin(regs['B'])}/{regs['B']}")
                print("====================")
            assert val == regs['B']%8
            #if len(out) >= len(ops):
            #    return None
            #print(f"printing operand {operand} {regs}={val}")
            out.append(val)
            if len(out)<=len(ops) and out[len(out)-1] == ops[len(out)-1]:
                #print(f"{origai} matches at position {len(out)-1}")
                pass
                #return None
        elif op == 6:
            val = regs['A']
            pow = parse_2nd_operand(operand)
            regs['B'] = val // (2**pow)
        elif op == 7:
            val = regs['A']
            pow = parse_2nd_operand(operand)
            assert pow == regs['B']
            if verbose:
                print(f"c= {regs['A']} // 2**{regs['B']} = {val // (2**pow)}")
            regs['C'] = val // (2**pow)

        i+=2
    return out, aas

#out = process(regs, ops)
#print(regs)
##print(out)
#print(",".join(str(x) for x in out ))
ai = 0
m = {}
if False:
    for ai in range(2000):
        #ai = 2**pow
        #if ai % 1000 == 0:
        #    print(ai)
        regs['A'] = ai
        out, aas = process(ai, regs, ops)
        #print(f"Len output = {len(out)} vs {len(ops)} for  {ai}")
        #time.sleep(2)

        print(out)
        print(aas)
        if 4 in out:
            raise Exception(f"ai={ai} out={out} aas={aas}")

        if out != ops:
            matches = [i for i in range(min(len(ops), len(out))) if out[i] == ops[i]]
            if len(matches) > 8:
                print(f"ai={ai} matches={matches}, len(out)={len(out)}, len(ops)={len(ops)}")
        if out is not None and out == ops:

            raise Exception(ai)
            break
        print(f"{out} for {ai} ({bin(ai)}")
        m[out[0]] = ai


#s = []
#for targ in ops:
#    s.append(bin(m[targ])[2:])
#print(s)

def binstitch(nums, binary=False):
    s = []
    if not binary:
        for targ in nums:
            #print(s)
            numstr = bin(targ)[2:]

            rnum = numstr.zfill(3)
            #rnum = rnum[::-1]
            s.append(rnum)
    else:
        for targ in nums:
           pass
    #print(len(s))
    #print("".join(s))
    return int("".join(s), 2)

def print_stitch(num):
    s = []
    while num:
        s.append(str(bin(num%8))[2:].zfill(3))
        num = num // 8
    s.reverse()
    #print(len(s))
    print('x'.join(s))


assert binstitch([7]*16) ==2**48-1

#sys.exit(0)


num = binstitch([2,3,5,3,5,3,1,7,1,3,5,4,5,7,5,6])

out, aas = process(num, regs, ops, False)
print(out)
print_stitch(num)


