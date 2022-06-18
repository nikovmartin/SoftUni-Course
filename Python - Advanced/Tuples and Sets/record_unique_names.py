count = int(input())
names = set()
for _ in range(count):
    current_name = input()
    if current_name not in names:
        print(current_name)
        names.add(current_name)

# count = int(input())
# names_set = {input() for _ in range(count)}
# [print(name) for name in names_set]