# text = input().split(", ")
# for user in text:
#     valid = True
#     if len(user) not in range(3, 17):
#         valid = False
#     for i in user:
#         if i.isalnum() is True or i == "_" or i == "-":
#             pass
#         else:
#             valid = False
#     if " " in user:
#         valid = False
#     if valid:
#         print(user)

import string
proper_elements = string.digits + string.ascii_letters + "_" + "-"
text = input().split(", ")
for user in text:
    valid = True
    if len(user) not in range(3, 17):
        valid = False
    for i in user:
        if i not in proper_elements:
            valid = False
    if valid:
        print(user)
