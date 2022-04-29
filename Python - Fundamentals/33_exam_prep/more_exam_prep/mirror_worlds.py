import re
regex = r"([@#])([a-zA-Z]{3,})\1{2}([a-zA-Z]{3,})\1"
mirror = []
counter = 0
text = input()
output = re.finditer(regex, text)
for match in output:
    first = match[2]
    second = match[3]
    counter += 1
    if first == second[::-1]:
        mirror.append(f"{first} <=> {second}")
if counter > 0:
    print(f"{counter} word pairs found!")
else:
    print("No word pairs found!")
if len(mirror) > 0:
    print("The mirror words are:")
    print(", ".join(mirror))
else:
    print("No mirror words!")