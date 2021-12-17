students = ['Ivan', 'Alex', 'Maria', 'Georgi']
scores = [5.00, 3.50, 5.50, 5.00]
students_score = dict(zip(students, scores))
print(students_score, '\n', '-'*53)

for k, v in students_score.items():
    if v == max(students_score.values()):
        print('{:8s} - {:.2f}'.format(k, v))

for k, v in students_score.items():
    if v == min(students_score.values()):
        print('{:8s} - {:.2f}'.format(k, v))