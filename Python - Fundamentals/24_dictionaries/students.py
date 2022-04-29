text = input()
courses = dict()

while ":" in text:
    (name, id, course) = text.split(":")
    if course not in courses:
        courses[course] = dict()
    courses[course][id] = name
    text = input()

if "_" in text:
    text = text.replace("_", " ")
if text in courses:
    for x in courses[text]:
        print(f"{courses[text][x]} - {x}")
