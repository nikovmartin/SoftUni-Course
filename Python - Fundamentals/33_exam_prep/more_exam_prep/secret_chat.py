message = input()
while True:
    command = input().split(":|:")
    if command[0] == "Reveal":
        break
    if command[0] == "InsertSpace":
        index = int(command[1])
        message = message[:index] + " " + message[index:]
        print(message)
    elif command[0] == "Reverse":
        substring = command[1]
        if substring in message:
            # first_index = message.find(substring)
            # last_index = first_index + len(substring)
            # message = message[:first_index] + substring[::-1] + message[last_index:]
            replacement = substring[::-1]
            message = message.replace(substring, "", 1)
            message += replacement
            print(message)
        else:
            print("error")
    elif command[0] == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        message = message.replace(substring, replacement)
        print(message)
print(f"You have a new text message: {message}")
