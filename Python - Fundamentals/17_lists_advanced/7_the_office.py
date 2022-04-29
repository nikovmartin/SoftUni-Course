# happiness = list(map(int, input().split(" ")))
# factor = int(input())
# happiness_multiplied = list(map(lambda x: x * factor, happiness))
# print(happiness_multiplied)

counter = 0
happiness = list(map(int, input().split(" ")))
factor = int(input())
happiness_multiplied = [x * factor for x in happiness]
happiness_filtered = list(filter(lambda x: x >= (sum(happiness_multiplied) / len(happiness_multiplied)),
                          happiness_multiplied))
if len(happiness_filtered) >= len(happiness_multiplied) / 2:
    print(f"Score: {len(happiness_filtered)}/{len(happiness_multiplied)}. Employees are happy!")
else:
    print(f"Score: {len(happiness_filtered)}/{len(happiness_multiplied)}. Employees are not happy!")

# average = sum(happiness_multiplied) / len(happiness_multiplied)
# for happy in happiness_multiplied:
#     if happy >= average:
#         counter += 1
# if counter >= len(happiness_multiplied):
#     print(f"Score: {counter}/{len(happiness_multiplied)}. Employees are happy!")
# else:
#     print(f"Score: {counter}/{len(happiness_multiplied)}. Employees are not happy!")