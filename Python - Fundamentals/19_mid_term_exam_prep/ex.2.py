array = list(map(int, input().split(" ")))

while True:
    explode = input().split(" ")
    command = explode[0]
    if command == "end":
        str_array = list(map(str, array))
        print(", ".join(str_array))
        break
    elif command == "swap":
        index_1 = int(explode[1])
        index_2 = int(explode[2])
        array[index_1], array[index_2] = array[index_2], array[index_1]
    elif command == "multiply":
        index_1 = int(explode[1])
        index_2 = int(explode[2])
        array[index_1] = array[index_1] * array[index_2]
    elif command == "decrease":
        array = [x - 1 for x in array]
