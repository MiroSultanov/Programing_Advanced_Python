number_of_students = int(input())
students_input = {}

for _ in range(number_of_students):
    student, grade = input().split()
    if student not in students_input:
        students_input[student] = []
    students_input[student].append(float(grade))

for student, grades in students_input.items():
    print(f"{student} ->", ' '.join([f'{x:.2f}' for x in grades]), f'(avg: {sum(grades)/len(grades):.2f})')