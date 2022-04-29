targets = list(map(int, input().split(" ")))

while True:
    explode = input().split(" ")
    if explode[0] == "End":
        targets = list(map(str, targets))
        print("|".join(targets))
        break
    index = int(explode[1])
    value = int(explode[2])
    if explode[0] == "Shoot":
        if 0 <= index < len(targets):
            targets[index] -= value
            if targets[index] <= 0:
                targets.pop(index)
    elif explode[0] == "Add":
        if 0 <= index < len(targets):
            targets.insert(index, value)
        else:
            print("Invalid placement!")
    elif explode[0] == "Strike":
        lowest_index = index - value
        highest_index = index + value
        if lowest_index >= 0 and highest_index < len(targets):
            targets = targets[:lowest_index] + targets[highest_index + 1:]
        else:
            print("Strike missed!")
