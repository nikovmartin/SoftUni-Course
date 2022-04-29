numbers_list = input().split(" ")
absolute_list = list()
for num in numbers_list:
    absolute_value = abs(float(num))
    absolute_list.append(absolute_value)
print(absolute_list)