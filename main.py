import sys
import re


def sqrt(number):
    x = number
    for _ in range(30):
        x = 0.5 * (x + number / x)
    return x


def format_number(number):
    if number == round(number):
        return str(int(round(number)))
    return f"{number:.6f}".rstrip("0").rstrip(".")


def polynomial_degree(coefficients):
    for i in range(len(coefficients) - 1, -1, -1):
        if coefficients[i] != 0:
            return i
    return 0


def no_degree(coefficients):
    if coefficients[0] != 0:
        print("No solution")
    else:
        print("Any real number is a solution.")


def first_degree(coefficients):
    print("Polynomial degree: 1")
    print("The solution is:")
    solution = -coefficients[0] / coefficients[1]
    print(f"{solution:.6f}")


def second_degree(coefficients):
    print("Polynomial degree: 2")

    a = coefficients[2]
    b = coefficients[1]
    c = coefficients[0]

    discriminant = b * b - 4 * a * c

    if discriminant > 0:
        print("Discriminant is strictly positive, the two solutions are:")
        root = sqrt(discriminant)
        x1 = (-b - root) / (2 * a)
        x2 = (-b + root) / (2 * a)
        print(f"{x1:.6f}")
        print(f"{x2:.6f}")

    elif discriminant == 0:
        print("Discriminant is equal to zero, the solution is:")
        solution = -b / (2 * a)
        print(f"{solution:.6f}")

    else:
        print("Discriminant is strictly negative, the two complex solutions are:")
        root = sqrt(-discriminant)
        real = -b / (2 * a)
        imaginary = root / (2 * a)

        print(f"{real:.6f}+{imaginary:.6f}i")
        print(f"{real:.6f}-{imaginary:.6f}i")


def solve_equation(coefficients):
    degree = polynomial_degree(coefficients)

    if degree == 0:
        no_degree(coefficients)
    elif degree == 1:
        first_degree(coefficients)
    elif degree == 2:
        second_degree(coefficients)
    else:
        print(f"Polynomial degree: {degree}")
        print("The polynomial degree is strictly greater than 2, I can't solve.")


def reduce_format(coefficients):
    degree = polynomial_degree(coefficients)
    result = ""

    for i in range(degree + 1):
        value = coefficients[i]
        term = f"{format_number(abs(value))} * X^{i}"

        if i == 0:
            result = f"-{term}" if value < 0 else term
        else:
            sign = "+" if value >= 0 else "-"
            result += f" {sign} {term}"

    return result + " = 0"


def parse_input(equation):
    coefficients_dict = {}
    left, right = equation.split("=")

    pattern = r"([+-]?)\s*(\d+(?:\.\d+)?)\s*\*\s*X\s*\^\s*(\d+)"

    def parse_side(part, side_sign):
        for sign, value, power in re.findall(pattern, part):
            coefficient = float(value)

            if sign == "-":
                coefficient *= -1

            degree = int(power)
            coefficients_dict[degree] = coefficients_dict.get(degree, 0) + side_sign * coefficient

    parse_side(left, 1)
    parse_side(right, -1)

    max_degree = max(coefficients_dict.keys(), default=0)
    coefficients = [0.0] * (max_degree + 1)

    for degree, value in coefficients_dict.items():
        coefficients[degree] = value

    return coefficients


def main():
    if len(sys.argv) == 2:
        equation = sys.argv[1]
    else:
        equation = sys.stdin.readline().strip()

    if not equation:
        return

    coefficients = parse_input(equation)

    print(f"Reduced form: {reduce_format(coefficients)}")
    solve_equation(coefficients)


if __name__ == "__main__":
    main()