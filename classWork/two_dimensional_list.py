test_list = [[0, 0, 0],
             [0, 0, 0]
             ]
for i, val in enumerate(test_list):
    for j, _ in enumerate(val):
        test_list[i][j] = 5
print(test_list, '\n')

for idx in range(len(test_list)):
    for idj in range(len(test_list[idx])):
        test_list[idx][idj] = 12
print(test_list)



