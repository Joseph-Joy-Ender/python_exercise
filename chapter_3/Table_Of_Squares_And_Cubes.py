print("number     square       cube")

# for i in range(1, 11):
#     square = i * i
#     cube = i * square
#     print(f'{i} \t     {square}      \t\t{cube}')


number = 1
while number <= 10:
    square_number = number * number
    cube_number = number * square_number
    print(f'{number} \t    \t{square_number}    \t\t{cube_number}')
    number += 1

