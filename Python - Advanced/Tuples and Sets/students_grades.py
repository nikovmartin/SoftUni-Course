def average(values):
    return sum(values) / len(values)


students_count = int(input())
gradebook = {}

for _ in range(students_count):
    student, grade = input().split(" ")
    if student not in gradebook:
        gradebook[student] = []
    gradebook[student].append(float(grade))

for student, grades in gradebook.items():
    txt_grades = " ".join(f"{grade:.2f}" for grade in grades)
    average_grade = average(grades)
    print(f'{student} -> {txt_grades} (avg: {average_grade:.2f})')