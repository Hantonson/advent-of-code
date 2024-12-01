file = open('../inputs/01.txt', 'r')

count_dico = {}

def find_count_of_elem(elem, list):
    if elem in count_dico.keys():
        return count_dico[elem]
    else:
        n_count = 0
        for e in list:
            if e == elem:
                n_count += 1
        count_dico[elem] = n_count
        return n_count

first_col = []
second_col = []
total_score = 0

for line in file:
    #line.replace('\n', '')
    data = str(line)
    v = data.split(';')
    first_col.append(int(v[0]))
    second_col.append(int(v[1]))



for n in first_col:
    total_score += n * find_count_of_elem(n, second_col)

print(total_score)