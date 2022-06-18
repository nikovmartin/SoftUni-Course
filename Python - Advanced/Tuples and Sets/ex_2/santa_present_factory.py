from collections import deque
boxes_values = deque([int(x) for x in input().split()])
magic_values = deque([int(x) for x in input().split()])
present_values = {
    "Doll": 150,
    "Wooden train": 250,
    "Teddy bear": 300,
    "Bicycle": 400
}
presents_crafted = {
    "Doll": 0,
    "Wooden train": 0,
    "Teddy bear": 0,
    "Bicycle": 0
}
while boxes_values and magic_values:
    box = boxes_values.pop()
    magic = magic_values.popleft()
    crafted = False
    for present in present_values:
        if present_values[present] == box * magic:
            crafted = True
            presents_crafted[present] += 1
            continue
    if not crafted:
        if box * magic < 0:
            boxes_values.append(box + magic)
            continue
        elif box * magic > 0:
            boxes_values.append(box + 15)
        else:
            if box == 0 and magic == 0:
                pass
            elif box == 0:
                magic_values.appendleft(magic)
            elif magic == 0:
                boxes_values.append(box)

if presents_crafted["Doll"] > 0 and presents_crafted["Wooden train"] > 0:
    print("The presents are crafted! Merry Christmas!")
elif presents_crafted["Teddy bear"] > 0 and presents_crafted["Bicycle"] > 0:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if boxes_values:
    print(f"Materials left: {', '.join([str(x) for x in reversed(boxes_values)])}")
if magic_values:
    print(f"Magic left: {', '.join([str(x) for x in magic_values])}")
for toy, amount in sorted(presents_crafted.items()):
    if amount > 0:
        print(f"{toy}: {amount}")