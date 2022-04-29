explode = input().split(">")
diff = 0
final_line = ""

final_line += explode[0]
for segment in explode[1:]:
    explosion = int(segment[0]) + diff
    diff = 0
    final_line += ">"
    if explosion > len(segment):
        diff = explosion - len(segment)
    final_line += segment[explosion:]

print(final_line)