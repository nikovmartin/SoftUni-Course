letter_count = int(input())
sum = 0
for i in range (1, letter_count + 1):
    current_letter = input()
    sum += ord(current_letter)
print(f"The sum equals: {sum}")