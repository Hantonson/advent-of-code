import re


def process_instructions(instructions):
    # Regex to find all `mul(a, b)` instructions
    mul_pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    # Regex to find all `don't()` and `do()` instructions
    control_pattern = re.compile(r"(don't\(\)|do\(\))")

    # Split the instructions into tokens based on `don't()` and `do()`
    tokens = control_pattern.split(instructions)

    enabled = True  # At the beginning, `mul` is enabled
    results = []

    for token in tokens:
        token = token.strip()
        if token == "don't()":
            enabled = False  # Disable `mul`
        elif token == "do()":
            enabled = True  # Enable `mul`
        else:
            # Find all `mul(a, b)` in the current token if `mul` is enabled
            if enabled:
                for match in mul_pattern.finditer(token):
                    a, b = map(int, match.groups())
                    results.append(a * b)

    return results


file = open('../inputs/03.txt', 'r')
instructions = file.read()
# Example input
#instructions = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

# Process the instructions and calculate the sum of enabled multiplications
result = sum(process_instructions(instructions))
print("Sum of enabled multiplications:", result)
