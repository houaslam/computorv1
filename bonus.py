import sys
import math
import re

# DEGREE 0
def no_degree(coefficients: list) -> None:
    if coefficients[0] != 0:
        print("No solution")
    else:
        print("Any real number is a solution.")

# DEGREE 1 
def first_degree(coefficients: list) -> None:
    print("Polynomial degree: 1")
    print("The solution is:")
    solution = -coefficients[0] / coefficients[1]
    print("{:.6f}".format(solution))
    
# DEGREE 2
def second_degree(coefficients: list) -> None:
    print("Polynomial degree: 2")

    descriminat =(coefficients[1] **2)  - 4 * coefficients[0]*coefficients[2]
    
    if descriminat < 0:
        descriminat *= -1
        descriminat = math.sqrt(descriminat)
        print("Discriminant is strictly negative, the two complex solutions are:")
        print("{:.6f}".format(-coefficients[1]/ (2 *coefficients[2])) + "+" +"{:.6f}".format(descriminat/ (2 *coefficients[2])) + "i")
        print("{:.6f}".format(-coefficients[1]/ (2 *coefficients[2])) + "-" +"{:.6f}".format(descriminat/ (2 *coefficients[2])) + "i")
    elif descriminat > 0:
        print("Discriminant is strictly positive, the two solutions are")
        descriminat = math.sqrt(descriminat)
    
        if descriminat > 0:
            firstSolution = (-coefficients[1] + descriminat) / (2 *coefficients[2])
            secondSolution = (-coefficients[1] - descriminat) / (2 *coefficients[2])
            print("{:.6f}".format(secondSolution))
            print("{:.6f}".format(firstSolution))
    else:
        solution = (-coefficients[1]) / (2 *coefficients[2])
        print("{:.6f}".format(solution))

def solve_equation(coefficients: list) -> None:
    if not coefficients[2] and not coefficients[1]:
        no_degree(coefficients)
    elif not coefficients[2]:
        first_degree(coefficients)
    elif coefficients[2] != 0 and len(coefficients) == 3:
        second_degree(coefficients)
        
def reduce_format(coefficients: list) -> str:
    reducedFormat = ""
    for i in reversed(range(len(coefficients))):
        if coefficients[i] != 0:
            if not reducedFormat:  # First term
                reducedFormat = f"{coefficients[i]} * X^{i}"
            else:  # Not first term
                if coefficients[i] > 0:
                    reducedFormat += f" + {coefficients[i]} * X^{i}"
                else:
                    reducedFormat += f" - {abs(coefficients[i])} * X^{i}"
    reducedFormat += " = 0"
    return reducedFormat


def parse_input(input):
    coefficients = [0,0, 0]
    equationParts = input.split("=")
    

    def match(input, sign):
        pattern = r"([+-]?)\s*(\d+(?:\.\d+)?)\s*\*\s*X\s*(?:\^\s*(\d+))"
        matchs = re.findall(pattern, input)
        for match in matchs:
            if int(match[2]) > 2:
                print("Polynomial degree: 3")
                print("The polynomial degree is strictly greater than 2, I can't solve.")
                exit(1)
            coefficients[int(match[2])] += sign * (float(match[1]) if '.' in match[1] else int(match[1])) * (-1 if match[0] == '-' else 1)

    match(equationParts[0], 1)
    match(equationParts[1], -1)
    return coefficients
        
if __name__ == "__main__":
    equationInput = sys.argv[1]
    coefficients=  parse_input(equationInput)
    print(f"Reduced form: {reduce_format(coefficients)}")
    solve_equation(coefficients)
        
        