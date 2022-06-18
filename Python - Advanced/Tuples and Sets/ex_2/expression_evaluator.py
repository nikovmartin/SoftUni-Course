# from collections import deque
# current_nums = deque()
# string = input().split(" ")
# calculation = 0
# for el in string:
#     if el not in "+-*/":
#         current_nums.append(int(el))
#     else:
#         while len(current_nums) > 1:
#             if el == "+":
#                 left = current_nums.popleft()
#                 right = current_nums.popleft()
#                 current_nums.appendleft(left + right)
#             elif el == "-":
#                 left = current_nums.popleft()
#                 right = current_nums.popleft()
#                 current_nums.appendleft(left - right)
#             elif el == "/":
#                 left = current_nums.popleft()
#                 right = current_nums.popleft()
#                 current_nums.appendleft(left // right)
#             elif el == "*":
#                 left = current_nums.popleft()
#                 right = current_nums.popleft()
#                 current_nums.appendleft(left * right)
# print(*current_nums, sep="")

from collections import deque
opearations = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "-/": lambda a, b: a // b
}
current_nums = deque()
string = input().split(" ")
calculation = 0
for el in string:
    if el not in "+-*/":
        current_nums.append(int(el))
    else:
        while len(current_nums) > 1:
            left = current_nums.popleft()
            right = current_nums.popleft()
            result = opearations[el](left, right)
            current_nums.appendleft(result)
print(current_nums.popleft())
