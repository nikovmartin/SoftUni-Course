numbers = input().split(" ")
rounded_list = list()
for number in numbers:
    rounded_list.append(round(float(number)))
print(rounded_list)
