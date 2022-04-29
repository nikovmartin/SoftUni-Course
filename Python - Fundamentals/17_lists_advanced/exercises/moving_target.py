sequence = list(map(int, input().split(" ")))

while True:
    explode = input().split(" ")
    command = explode[0]
    if command == "End":
        sequence = list(map(str, sequence))
        print("|".join(sequence))
        break
    index = int(explode[1])

    if command == "Shoot" and index in range(len(sequence)):
        power = int(explode[2])
        sequence[index] -= power
        if sequence[index] <= 0:
            sequence.pop(index)

    elif command == "Add":
        if index in range(len(sequence)):
            value = int(explode[2])
            sequence.insert(index, value)
        else:
            print("Invalid placement!")

    elif command == "Strike":
        radius = int(explode[2])
        lowest_index = index - radius
        highest_index = index + radius
        if highest_index in range(len(sequence)) and lowest_index in range(len(sequence)):
            sequence = sequence[0:lowest_index] + sequence[highest_index + 1::]
        else:
            print("Strike missed!")