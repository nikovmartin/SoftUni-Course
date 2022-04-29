courses_dict = {}
command = input().split(" : ")
while command[0] != "end":
    course = command[0]
    student = command[1]
    if course not in courses_dict:
        courses_dict[course] = []
    courses_dict[course].append(student)
    command = input().split(" : ")
for course in courses_dict:
    print(f"{course}: {len(courses_dict[course])}")
    for student in courses_dict[course]:
        print(f"-- {student}")
