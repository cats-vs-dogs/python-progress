students = ['Ivan', 'Alex', 'Maria', 'Georgi']
scores = [5.00, 3.50, 5.50, 5.00]
students_score = dict(zip(students, scores))
print(students_score, '\n', '-'*53)

best_students_score = {}
for k, v in students_score.items():
    if v > 4:
        best_students_score[k] = v

# dict comprehension
best_student_scores_2 = {k:v for (k, v) in students_score.items() if v > 4}

print(best_students_score, '\n', '-'*53)
print(best_student_scores_2, '\n', '-'*53)

        
for k, v in best_students_score.items():
    print('{:8s} - {:.2f}'.format(k, v))