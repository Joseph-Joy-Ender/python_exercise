def average(student_score):
    return sum(student_score) / len(student_score)


scores = []
for i in range(0, 10):
    score = int(input("Enter ten scores: "))
    scores.append(score)


print(average(scores))