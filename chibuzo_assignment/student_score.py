#score_counter = 1
#total = 0
#average = 0

#while score_counter <= 10:
 #   score = int(input("Enter student score: "))
  #  total += score
   #  score_counter += 1
# average = total / score_counter
# print(average)


score = int(input("Enter student score and press -1 to stop: "))
score_counter = 0
total = 0
average = 0

while score != -1:
    total += score
    score_counter += 1
    score = int(input("Enter student grade and press -1 to stop: "))

average = total / score_counter
print("Total average is ", average)
print(f"{average:.2f}")
