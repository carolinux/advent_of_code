
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
out = []

print(regs)
#print(ops)

i = 0


while i<len(ops):
    op = ops[i]
    operand = ops[i+1]
    if op == 0:
        val = regs['A']
        pow = parse_2nd_operand(operand)
        regs['A'] = val // (2**pow)
    elif op == 1:
        val = regs['B']
        val2 = operand
        regs['B'] = val ^ val2
    elif op == 2:
        val = parse_2nd_operand(operand) % 8
        regs['B'] = val
    elif op == 3:
        if regs['A'] == 0:
            i+=2
            continue
        else:
            i = operand
            continue
    elif op == 4:
        regs['B'] = regs['B'] ^ regs['C']
    elif op == 5:
        val = parse_2nd_operand(operand) % 8
        out.append(val)
    elif op == 6:
        val = regs['A']
        pow = parse_2nd_operand(operand)
        regs['B'] = val // (2**pow)
    elif op == 7:
        val = regs['A']
        pow = parse_2nd_operand(operand)
        regs['C'] = val // (2**pow)


    i+=2


print(regs)
print(",".join(str(x) for x in out ))
