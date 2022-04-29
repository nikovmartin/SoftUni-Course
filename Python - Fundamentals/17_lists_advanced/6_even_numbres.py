numbers = list(map(int, input().split(", ")))
numbers_filtered = [num if num % 2 == 0 else "odd" for num in numbers]
final_filtered = []
for i in range(len(numbers_filtered)):
    if numbers_filtered[i] != "odd":
        final_filtered.append(i)
print(final_filtered)

