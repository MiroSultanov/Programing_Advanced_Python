# Write a program that reads students' names and their grades and adds them to the student record.
# On the first line, you will receive the number of students – N. On the following N lines, you will be receiving a student's name and their grade.
# For each student print all his/her grades and finally his/her average grade, formatted to the second decimal point in the 
# format: "{student's name} -> {grade1} {grade2} ... {gradeN} (avg: {average_grade})".
# The order in which we print the result does not matter.


number_of_students = int(input())
students_input = {}

for _ in range(number_of_students):
    student, grade = input().split()
    if student not in students_input:
        students_input[student] = []
    students_input[student].append(float(grade))

for student, grades in students_input.items():
    print(f"{student} ->", ' '.join([f'{x:.2f}' for x in grades]), f'(avg: {sum(grades)/len(grades):.2f})')
