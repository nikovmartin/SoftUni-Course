# import re
# total_calories = 0
# groceries = list()
# text = input()
# logic = r"([\|\#])([a-zA-Z ]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d+)\1"
# all_data = re.finditer(logic, text)
# for data in all_data:
#     item_name = data[2]
#     expiration = data[3]
#     calories = int(data[4])
#     total_calories += calories
#     groceries += [item_name, expiration, calories]
# days = int(total_calories / 2000)
# print(f"You have food to last you for: {days} days!")
# for i in range(0, len(groceries), 3):
#     print(f"Item: {groceries[i]}, Best before: {groceries[i+1]}, Nutrition: {groceries[i+2]}")
#
import re
total_calories = 0
groceries = list()
text = input()
logic = r"([\|\#])([a-zA-Z ]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d+)\1"
all_data = re.finditer(logic, text)
for data in all_data:
    item_name = data[2]
    expiration = data[3]
    calories = int(data[4])
    total_calories += calories
    groceries.append([item_name, expiration, calories])
days = int(total_calories / 2000)
print(f"You have food to last you for: {days} days!")
for product in groceries:
    print(f"Item: {product[0]}, Best before: {product[1]}, Nutrition: {product[2]}")
