# import re
#
# while True:
#     text = input()
#     if not text:
#         break
#     matches = re.findall(r"\d+", text)
#     if len(matches) > 0:
#         print(' '.join(matches), end=" ")


import re
output = list()
while True:
    text = input()
    if not text:
        break
    matches = re.finditer(r"\d+", text)
    for match in matches:
        output.append(match.group())
print(" ".join(output))
