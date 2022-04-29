collectibles = input().split(", ")
while True:
    commands = input().split(" - ")
    command = commands[0]
    if command == "Craft!":
        print(", ".join(collectibles))
        break
    if command == "Collect":
        if commands[1] not in collectibles:
            collectibles.append(commands[1])
    elif command == "Drop":
        if commands[1] in collectibles:
            collectibles.remove(commands[1])
    elif command == "Combine Items":
        combined = commands[1]
        combined = combined.split(":")
        if combined[0] in collectibles:
            index_old_element = collectibles.index(combined[0])
            collectibles.insert(index_old_element + 1, combined[1])
    elif command == "Renew":
        if commands[1] in collectibles:
            collectibles.remove(commands[1])
            collectibles.append(commands[1])
