import sys
import re
import math

def parse_input():
    data = []
    current_set = {}

    for line in sys.stdin:
        line = line.strip()
        if not line:
            # Empty line indicates the end of a set
            if current_set:
                data.append(current_set)
                current_set = {}
        else:
            # Match "Button A: X+<value>, Y+<value>" or "Prize: X=<value>, Y=<value>"
            match = re.match(r"(?P<type>Button [AB]|Prize): X[+=](?P<x>\d+), Y[+=](?P<y>\d+)", line)
            if match:
                obj_type = match.group("type")
                x = int(match.group("x"))
                y = int(match.group("y"))
                current_set[obj_type] = {"X": x, "Y": y}

    # Add the last set if any
    if current_set:
        data.append(current_set)

    return data


def main():
    parsed_data = parse_input()
    costA = 3
    costB = 1
    ans = 0
    for index, entry in enumerate(parsed_data):
        ax = entry["Button A"]["X"]
        ay = entry["Button A"]["Y"]
        bx = entry["Button B"]["X"]
        by = entry["Button B"]["Y"]
        px = entry["Prize"]["X"]
        py = entry["Prize"]["Y"]
        mincost = math.inf
        for i in range(100):
            for j in range(100):
                x  = i * ax + j * bx
                y = i * ay + j * by
                if x == px and y == py:
                    cand = i * costA + j * costB
                    mincost = min(mincost, cand)

        if mincost != math.inf:
            ans+=mincost

    print(ans)


if __name__ == "__main__":
    main()
