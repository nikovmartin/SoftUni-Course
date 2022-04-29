gifts = input().split(" ")
copy_gifts = gifts.copy()
final_gifts = list()
command = input()
counter = -1
while command != "No Money":
    separated_command = command.split(" ")
    status = separated_command[0]
    if status == "OutOfStock":
        for i in copy_gifts:
            counter += 1
            if i == separated_command[1]:
                copy_gifts[counter] = "None"
    elif status == "Required":
        if 0 < int(separated_command[2]) < len(copy_gifts):
            index = int(separated_command[2])
            copy_gifts[index] = separated_command[1]
    elif status == "JustInCase":
        copy_gifts[-1] = separated_command[1]
    command = input()
    counter = -1

while "None" in copy_gifts:
    copy_gifts.remove("None")

for i in copy_gifts:
    print(i, end=" ")
