current = input().split(".")
updated = int("".join(current)) + 1
list_updated_strings = [num for num in str(updated)]
result = ".".join(list_updated_strings)
print(result)


# def update(version_number):
#     version_number = int("".join(version_number)) + 1
#     list_updated_strings = [num for num in str(version_number)]
#     result = ".".join(list_updated_strings)
#     return(result)
#
#
# data = input().split(".")
# print(update(data))

