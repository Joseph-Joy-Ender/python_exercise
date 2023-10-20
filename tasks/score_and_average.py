score = [[25, 50, 75],
         [40, 50, 60],
         [75, 65, 80]]
sums = 0
average = 0
for row in range(len(score)):
    for col in range(len(score[row])):
        sums += score[row][col]
        average = sums / len(score)
print(average)
print(sums)

rows = len(score)
tot = []
columns = len(score[0])
for i in range(columns):
    sumCol = 0
    for j in range(len(score)):
        tot = i
        sumCol += j * i
    print(sumCol)
