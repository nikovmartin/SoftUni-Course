from collections import deque

words = deque(input().split(" "))

main_colors = {"red", "yellow", "blue"}
secondary_colors = {"orange", "purple", "green"}

colors_found = []

while words:
    left = words.popleft()
    right = words.pop() if words else ""

    result = left + right
    if result in main_colors or result in secondary_colors:
        colors_found.append(result)
        continue

    result = right + left
    if result in main_colors or result in secondary_colors:
        colors_found.append(result)
        continue

    left = left[:-1]
    right = right[:-1]

    if left:
        words.insert(len(words) // 2, left)
    if right:
        words.insert(len(words) // 2, right)

result = []

for color in colors_found:
    if color in main_colors:
        result.append(color)
    elif color == "orange":
        if "red" in colors_found and "yellow" in colors_found:
            result.append(color)
    elif color == 'purple':
        if "red" in colors_found and "blue" in colors_found:
            result.append(color)
    elif color == 'green':
        if "yellow" in colors_found and "blue" in colors_found:
            result.append(color)

print(result)