# def even_odd(*args):
#     if args[-1] == "even":
#         even_list = []
#         for idx in range(len(args)-1):
#             if args[idx] % 2 == 0:
#                 even_list.append(args[idx])
#         return even_list
#     if args[-1] == "odd":
#         odd_list = []
#         for idx in range(len(args)-1):
#             if not args[idx] % 2 == 0:
#                 odd_list.append(args[idx])
#         return odd_list
#
#
# print(even_odd(1, 2, 3, 4, 5, 6, "even"))


def even_odd(*args):
    final_list = []
    parity = 0 if args[-1] == "even" else 1
    for idx in range(len(args) - 1):
        if args[idx] % 2 == parity:
            final_list.append(args[idx])
    return final_list


print(even_odd(1, 2, 3, 4, 5, 6, "even"))