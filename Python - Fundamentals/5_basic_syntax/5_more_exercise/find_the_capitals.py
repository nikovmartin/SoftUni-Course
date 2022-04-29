# string = str(input())
# upper_index = list()
# for i in range(len(string)):
#     current_letter = string[i]
#     ascii_letter = ord(current_letter)
#     if ascii_letter < 95:
#         upper_index.append(i)
# print(upper_index)

string = str(input())
upper_index = list()
for i in range(len(string)):
    current_letter = string[i]
    if current_letter.isupper():
        upper_index.append(i)
print(upper_index)