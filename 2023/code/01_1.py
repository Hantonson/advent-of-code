data = open("../inputs/01.txt","r")

digits = ["1","2","3","4","5","6","7","8","9","0"]
sum_01 = 0
for line in data:
    for c in line:
        if c in digits:
            sum_01 += (int(c) * 10)
            break
    for c in line[::-1]:
        if c in digits:
            sum_01 += int(c)
            break
data.close()

print(sum_01)