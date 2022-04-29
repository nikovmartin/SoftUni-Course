# count = {}
# text = input()
# for char in text:
#     if char == " ":
#         pass
#     elif char not in count:
#         count[char] = 1
#     else:
#         count[char] += 1
# for char in count:
#     print(f"{char} -> {count[char]}")

# count = {}
# text = input()
# for char in text:
#     if char == " ":
#         pass
#     elif char not in count:
#         count[char] = 1
#     else:
#         count[char] += 1
# for char, values in count.items():
#     print(f"{char} -> {values}")

from collections import Counter
text = input()
count = Counter(text)
for char, values in count.items():
    if char != " ":
        print(f"{char} -> {values}")