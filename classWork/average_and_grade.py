def get_average_score(scores):
    # compute sum of scores
    total = sum(scores)

    # get the number of subjects
    count = len(scores)

    # compute average score
    average_score_of_student = total / count

    return average_score_of_student


# Returns the grade based on the average score
def compute_grade(average_scores):
    if average_score >= 80.0:
        grades = 'A'
    elif average_score >= 60.0:
        grades = 'B'
    elif average_score >= 50.0:
        grades = 'C'
    else:
        grades = 'F'

    return grades


student_scores = [55, 64, 75, 80, 65]

# get average score
average_score = get_average_score(student_scores)

# get grade
grade = compute_grade(average_score)

print('Average score is', average_score)
print('Grade:', grade)
