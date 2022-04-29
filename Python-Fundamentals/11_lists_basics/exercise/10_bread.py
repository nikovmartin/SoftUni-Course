# energy = 100
# coins = 100
# initial_data = input().split("|")
# opened = True
# for i in range(len(initial_data)):
#     task_and_number = initial_data[i].split("-")
#     task = task_and_number[0]
#     number = int(task_and_number[1])
#     if "rest" in initial_data[i]:
#         if energy + number > 100:
#             print(f"You gained 0 energy.")
#         else:
#             energy += number
#             print(f"You gained {number} energy.")
#         print(f"Current energy: {energy}.")
#     elif "order" in initial_data[i]:
#         if energy >= 30:
#             energy -= 30
#             coins += number
#             print(f"You earned {number} coins.")
#         else:
#             print("You had to rest!")
#             energy += 50
#     else:
#         if coins >= number:
#             coins -= number
#             print(f"You bought {task}.")
#         else:
#             print(f"Closed! Cannot afford {task}.")
#             opened = False
#             break
#
# if opened:
#     print("Day completed!")
#     print(f"Coins: {coins}")
#     print(f"Energy: {energy}")

energy = 100
coins = 100
initial_data = input().split("|")
opened = True
for data in initial_data:
    task_and_number = data.split("-")
    task = task_and_number[0]
    number = int(task_and_number[1])
    if task == "rest":
        if energy + number > 100:
            print(f"You gained 0 energy.")
        else:
            energy += number
            print(f"You gained {number} energy.")
        print(f"Current energy: {energy}.")
    elif task == "order":
        if energy >= 30:
            energy -= 30
            coins += number
            print(f"You earned {number} coins.")
        else:
            print("You had to rest!")
            energy += 50
    else:
        if coins >= number:
            coins -= number
            print(f"You bought {task}.")
        else:
            print(f"Closed! Cannot afford {task}.")
            opened = False
            break

if opened:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")