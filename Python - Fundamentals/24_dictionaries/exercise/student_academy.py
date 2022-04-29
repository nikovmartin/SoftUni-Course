people_count = int(input())
gradebook = {}
for i in range(people_count):
    person = input()
    grade = float(input())

    if person not in gradebook:
        gradebook[person] = [grade, 1]
    else:
        gradebook[person] = [gradebook[person][0] + grade, gradebook[person][1] + 1]

for person in gradebook:
    average_grade = gradebook[person][0] / gradebook[person][1]
    if average_grade >= 4.5:
        print(f"{person} -> {average_grade:.2f}")
print(gradebook.keys())