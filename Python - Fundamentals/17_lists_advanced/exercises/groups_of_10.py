# numbers = list(map(int, input().split(", ")))
# groups = max(numbers) // 10
# counter = 10
# for number in numbers:
#     ten = [int(number) for number in numbers if int(number) <= counter]
#         print(f""Group of 10's: {list_of_numbers}".")
#     twenty = [int(number) for number in numbers if 11 <= int(number) < 21]
#     thirty = [int(number) for number in numbers if 21 <= int(number) < 31]
#     forty = [int(number) for number in numbers if 31 <= int(number) < 41]
#     fifty = [int(number) for number in numbers if 41 <= int(number) < 51]
# # print(f""Group of {group}'s: {list_of_numbers}".")


numbers = list(map(int, input().split(", ")))
if max(numbers) % 10 == 0:
    groups = max(numbers) // 10
else:
    groups = max(numbers) // 10 + 1
counter = 10
for i in range(groups):
    list_of_numbers = [int(number) for number in numbers if int(number) <= counter]
    print(f"Group of {counter}'s: {list_of_numbers}")
    numbers = list(filter(lambda x: x > counter, numbers))
    counter += 10
    list_of_numbers =[]


