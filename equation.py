import math
import sys


def solve_quadratic(a: float, b: float, c: float) -> list:
    print(f"Equation is: ({a}) x^2 + ({b}) x + ({c}) = 0")

    discriminant = b**2 - 4 * a * c
    if discriminant > 0:
        x1 = (-b - math.sqrt(discriminant)) / (2 * a)
        x2 = (-b + math.sqrt(discriminant)) / (2 * a)
        return [x1, x2]
    elif discriminant == 0:
        x = -b / (2 * a)
        return [x]
    else:
        return []


def print_result(roots: list):
    if len(roots) == 0:
        print("There are 0 roots")
    elif len(roots) == 1:
        print("There are 1 roots")
        print(f"x1 = {roots[0]}")
    else:
        print("There are 2 roots")
        print(f"x1 = {roots[0]}")
        print(f"x2 = {roots[1]}")


def get_coefficient_value(coeff_name: str) -> float:
    while True:
        value = input(coeff_name)
        try:
            result = float(value)
            return result
        except ValueError:
            print(f"Error. Expected a valid real number, got {value} instead")


def start_interactive_mode():
    a = get_coefficient_value("a = ")
    while a == 0:
        print("Error. a cannot be 0")
        a = get_coefficient_value("a = ")
    b = get_coefficient_value("b = ")
    c = get_coefficient_value("c = ")

    roots = solve_quadratic(a, b, c)
    print_result(roots)


def start_file_mode(filepath: str):
    try:
        with open(filepath, "r") as f:
            content = f.read().strip()
        parts = content.split()
        if len(parts) != 3:
            raise ValueError("invalid file format")
        a, b, c = map(float, parts)
        if a == 0:
            print("Error. a cannot be 0")
            sys.exit(1)
        roots = solve_quadratic(a, b, c)

        print_result(roots)
    except FileNotFoundError:
        print(f"file {filepath} does not exist")
        sys.exit(1)
    except ValueError as err:
        print(f"{err}")
        sys.exit(1)


def main():
    if len(sys.argv) == 1:
        start_interactive_mode()
    else:
        start_file_mode(sys.argv[1])


if __name__ == "__main__":
    main()
