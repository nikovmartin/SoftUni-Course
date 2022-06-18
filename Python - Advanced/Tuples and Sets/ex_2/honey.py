from collections import deque

calculation = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y
}
total_honey = 0

working_bees = deque([int(x) for x in input().split(" ")])
nectar = deque([int(x) for x in input().split(" ")])
symbols = deque(input().split(" "))
while nectar and working_bees:
    if nectar[-1] >= working_bees[0]:
        if nectar[-1] == 0:
            working_bees.popleft()
            nectar.pop()
            continue
        total_honey += abs(calculation[symbols[0]](working_bees[0], nectar[-1]))
        working_bees.popleft()
        nectar.pop()
        symbols.popleft()
    else:
        nectar.pop()

print(f"Total honey made: {total_honey}")
if working_bees:
    print(f"Bees left: {', '.join([str(x) for x in working_bees])}")
if nectar:
    print(f"Nectar left: {', '.join([str(x) for x in nectar])}")