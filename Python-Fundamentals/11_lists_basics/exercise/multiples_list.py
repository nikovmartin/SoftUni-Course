initial_number = int(input())
times = int(input())
list = list()
current_number = 0
for i in range(times):
    current_number += initial_number
    list.append(current_number)
print(list)