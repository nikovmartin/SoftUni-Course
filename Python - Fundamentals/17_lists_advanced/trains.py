wagons = int(input())
train = [0 for i in range(wagons)]
command = input()
while command != "End":
    explode = command.split(" ")
    current_command = explode[0]
    if current_command == "add":
        num_people = int(explode[1])
        train[-1] += num_people
    if current_command == "insert":
        index = int(explode[1])
        num_people = int(explode[2])
        train[index] += num_people
    if current_command == "leave":
        index = int(explode[1])
        num_people = int(explode[2])
        train[index] -= num_people
    command = input()
print(train)