import re


def extract_combined_number(input_string):
    # Mapping of spelled-out numbers to numeric equivalents
    spelled_to_digit = {
        "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
        "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
    }

    # Regex to match spelled-out numbers or numeric digits
    pattern = r'zero|one|two|three|four|five|six|seven|eight|nine|\d'

    # List to hold matched digits
    digits = []
    while True:
        # Find the first match
        match = re.search(pattern, input_string, flags=re.IGNORECASE)
        if not match:
            break  # No more matches, exit loop

        # Normalize match to a digit and append to the list
        match_text = match.group(0)
        digits.append(spelled_to_digit[match_text.lower()] if match_text.lower() in spelled_to_digit else match_text)

        # Remove the matched portion from the string
        input_string = input_string[match.end():]

    if not digits:
        return None  # Return None if no digits are found

    # Combine the first and last digits
    combined_number = digits[0] + digits[-1]
    return int(combined_number)

# Example Usage
in_string = "eighthree."
result = extract_combined_number(in_string)
print(f"Combined number: {result}")
data = open("../inputs/01.txt","r")

sum_02 = 0
for line in data:
    number = extract_combined_number(line)
    print(f"${line}: {number}")
    #sum_02 += number
data.close()
#54627
print(sum_02)





