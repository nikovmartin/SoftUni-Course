command = input()
phonebook = {}

while "-" in command:
    explode = command.split("-")
    name = explode[0]
    phone = explode[1]
    phonebook[name] = phone
    command = input()

command = int(command)
for i in range(command):
    name = input()
    if name in phonebook:
        print(f"{name} -> {phonebook[name]}")
    else:
        print(f"Contact {name} does not exist.")