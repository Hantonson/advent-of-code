file = open('../inputs/01.txt', 'r')

first_col = []
second_col = []
total_distance = 0

for line in file:
    #line.replace('\n', '')
    data = str(line)
    v = data.split(';')
    first_col.append(int(v[0]))
    second_col.append(int(v[1]))

first_col.sort()
second_col.sort()

for i in range(len(first_col)):
    total_distance += abs(first_col[i] - second_col[i])

print(total_distance)