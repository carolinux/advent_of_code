import sys
import re
import math
from sympy import symbols, diophantine, linsolve, Eq

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
        px = entry["Prize"]["X"] + 10000000000000
        py = entry["Prize"]["Y"] + 10000000000000
        x, y = symbols('x y', integer=True, positive=True)
        if ax/ay == bx/by and px/py == ax/ay:
            raise Exeption("Infinite solutions")
            continue

        eq1 = Eq(ax * x + bx * y - px)

        eq2 = Eq(ay * x + by * y - py)

        # Solve the Diophantine system
        solutions = linsolve([eq1, eq2], (x, y))
        for sol in solutions:
            x_sol, y_sol = sol
            if x_sol.is_Integer and y_sol.is_Integer:
                assert x_sol >= 0 and y_sol >= 0
                print(f"Integer solution: x = {x_sol}, y = {y_sol}")
                ans += x_sol * costA + y_sol * costB
            else:
                print("No integer solutions found.")



    print(ans)


if __name__ == "__main__":
    main()
