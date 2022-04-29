encrypted = input()
while True:
    command = input().split("|")
    if command[0] == "Decode":
        break
    if command[0] == "Move":
        n = int(command[1])
        encrypted = encrypted[n:] + encrypted[:n]
        # beginning = list()
        # end = list()
        # for i in range(len(encrypted)):
        #     if n > i:
        #         beginning.append(encrypted[i])
        #     else:
        #         end.append(encrypted[i])
        # encrypted = "".join(end + beginning)
    elif command[0] == "Insert":
        index = int(command[1])
        value = command[2]
        encrypted = encrypted[:index] + value + encrypted[index:]
    elif command[0] == "ChangeAll":
        encrypted = encrypted.replace(command[1], command[2])
print(f"The decrypted message is: {encrypted}")