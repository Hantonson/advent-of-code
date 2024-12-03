import re

# Your long string
data = open('../inputs/03.txt','r')

muls = []

# Regular expression to match "mul(<number>,<number>)"
pattern = r"mul\((\d{1,3}),(\d{1,3})\)"


for line in data:
    matches = re.findall(pattern, line)
    # Print the matches
    print(matches)
    muls.append(matches)

total_sum = 0
for mul in muls:
    total_sum += sum(int(a) * int(b) for a, b in mul)

print(total_sum)
