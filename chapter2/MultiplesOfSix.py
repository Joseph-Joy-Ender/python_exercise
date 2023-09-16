   # total = 1
   # count = 0
 # for i in range(1, 3000):
   # total = 6 * i
   # count += 1
   # print(total, end=" ")

number = 1
count = 1
while count <= 3000:
    count += 6
    number *= 6
    if number >= 3000:
        break
    print(number, end=" ")
