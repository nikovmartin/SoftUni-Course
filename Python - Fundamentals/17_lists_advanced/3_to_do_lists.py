unordered_list = ["" for i in range(11)]
command = input()
while command != "End":
    explode = command.split("-")
    importance = int(explode[0])
    note = explode[1]
    unordered_list[importance] = note
    command = input()
ordered_list = [task for task in unordered_list if task != ""]
print(ordered_list)