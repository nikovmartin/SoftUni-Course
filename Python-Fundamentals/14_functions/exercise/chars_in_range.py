# a = input()
# b = input()
# in_between_list = list()
# for i in range(ord(a) + 1,ord(b)):
#     in_between_list.append(chr(i))
# print(in_between_list)


# def function(a, b):
#     in_between_list = list()
#     for i in range(ord(a) + 1, ord(b)):
#         in_between_list.append(chr(i))
#     output = " ".join(in_between_list)
#     return output
#
#
# a = input()
# b = input()
# print(function(a, b))


def function(a, b):
    for i in range(ord(a) + 1, ord(b)):
        print(chr(i), end=" ")


a = input()
b = input()
function(a, b)