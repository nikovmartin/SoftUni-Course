initial_pass = input()
current_version = initial_pass
odds = list()
final_version = ""
while True:
    command = input().split(" ")
    if command[0] == "Done":
        print(f"Your password is: {current_version}")
        break
    if command[0] == "TakeOdd":
        for i in range(len(current_version)):
            if i % 2 != 0:
                final_version += current_version[i]
        current_version = final_version
        print(current_version)
    elif command[0] == "Cut":
        index = int(command[1])
        length = int(command[2])
        text_to_remove = current_version[index:index + length]
        current_version = current_version.replace(text_to_remove, "", 1)
        print(current_version)
    elif command[0] == "Substitute":
        substring = command[1]
        substitute = command[2]
        if substring in current_version:
            current_version = current_version.replace(substring, substitute)
            print(current_version)
        else:
            print("Nothing to replace!")
