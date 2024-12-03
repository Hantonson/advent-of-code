def brute_force_valid(i_array):
    correct = isValidArray(i_array)
    if not correct:
        for i in range(len(i_array)):
            new_array = i_array[:]
            new_array.pop(i)
            print('Trying with', new_array )
            correct = isValidArray(new_array)
            print('Result', new_array )
            if correct:
                break
    return correct

def isValidArray(i_array):
    correct = True
    order = None # asc(0) or desc(1)
    for i in range(1,len(i_array)):
        if not correct:
            break
        if order == None:
            order = 0 if i_array[i] < i_array[i-1] else 1
        else:
            correct = (order == 0 and i_array[i] < i_array[i-1]) or (order == 1 and i_array[i] > i_array[i-1])
        if i_array[i] == i_array[i-1] or abs(i_array[i] - i_array[i-1]) > 3:
            correct = False

    return correct

def toIntArray(v):
    i = []
    for s in v:
        i.append(int(s))
    return i




_input = open('../inputs/02.txt', 'r')

total_correct = 0
for line in _input:
    nums = line.split(' ')
    nums_array = toIntArray(nums)
    if brute_force_valid(nums_array):
        total_correct += 1

print(total_correct)