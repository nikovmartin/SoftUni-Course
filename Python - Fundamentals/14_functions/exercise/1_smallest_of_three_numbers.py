# def minimum_number(a, b, c):
#     current_min = a
#     if b < a:
#         current_min = b
#     if c < b:
#         current_min = c
#     return current_min
#
#
# num_1 = int(input())
# num_2 = int(input())
# num_3 = int(input())
#
# print(minimum_number(num_1, num_2, num_3))


def minimum_number(a, b, c):
    return min(a, b, c)


num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

print(minimum_number(num_1, num_2, num_3))