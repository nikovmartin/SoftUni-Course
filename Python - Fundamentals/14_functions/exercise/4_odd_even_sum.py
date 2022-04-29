# def odd_even_sum(nums):
#     odd_count = 0
#     even_count = 0
#     for num in nums:
#         if int(num) % 2 == 0:
#             even_count += int(num)
#         else:
#             odd_count += int(num)
#     return f"Odd sum = {odd_count}, Even sum = {even_count}"
#
#
# number = input()
# print(odd_even_sum(number))


def odd_even_sum(nums):
    odd_count = 0
    even_count = 0
    for num in nums:
        if num % 2 == 0:
            even_count += num
        else:
            odd_count += num
    return f"Odd sum = {odd_count}, Even sum = {even_count}"


number = map(int, list(input()))
print(odd_even_sum(number))

