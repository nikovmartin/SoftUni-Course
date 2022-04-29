deck = input().split(" ")
times_shuffled = int(input())
length = len(deck)

middle_index = length // 2

first_half = deck[:middle_index]
second_half = deck[middle_index:]

shuffled = list()
for k in range(times_shuffled):
    shuffled.clear()
    for i in range(len(first_half)):
        shuffled.append(first_half[i])
        shuffled.append(second_half[i])
    first_half = shuffled[:middle_index]
    second_half = shuffled[middle_index:]


print(shuffled)