import math

def solve_quadratic(a, b, c):
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
    
def print_result(roots):
    if len(roots) == 0:
        print("There are 0 roots")
    elif len(roots) == 1:
        print("There are 1 roots")
        print(f"x1 = {roots[0]}")
    else:
        print("There are 2 roots")
        print(f"x1 = {roots[0]}")
        print(f"x2 = {roots[1]}")
    
def get_float(float_num):
    while True:
        value = input(float_num)
        try:
            result = float(value)
            return result
        except ValueError:
            print(f"Error. Expected a valid real number, got {value} instead")

def interactive_mode():
    a = get_float("a = ")
    while a == 0:
        print("Error. a cannot be 0")
        a = get_float("a = ")
    b = get_float("b = ")
    c = get_float("c = ")
    
    print(f"Equation is: ({a}) x^2 + ({b}) x + ({c}) = 0")
    roots = solve_quadratic(a, b, c)
    print_result(roots)

def main():
    interactive_mode()
    # (5, 3, -26) – "-2.6 and 2.0"
    # (1, 2, 3) – "There are 0 roots"
    # (1, 2, 1) – "-1.0"

if __name__ == "__main__":
    main()