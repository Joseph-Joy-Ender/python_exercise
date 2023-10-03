scores = []
largestScore = 0
for i in range(0, 10):
    score = int(input("Enter ten scores: "))
    if score > largestScore:
        largestScore = score
    scores.append(score)
print(scores)
print('The largest score is', largestScore)
