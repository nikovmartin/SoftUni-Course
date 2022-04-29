numbers = input().split(" ")
copy_numbers = list(map(int, numbers))
n = int(input())
for i in range(n):
    current_lowest = min(copy_numbers)
    copy_numbers.remove(current_lowest)
    numbers.remove(str(current_lowest))

print(", ".join(numbers))
